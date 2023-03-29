import os
import threading
from hashlib import sha256
from typing import Dict, Optional, Union, cast

from chaosaddons.controls import safeguards
from chaoslib.run import EventHandlerRegistry, RunEventHandler
from chaoslib.types import (
    Configuration,
    Experiment,
    Extension,
    Journal,
    Secrets,
)
from logzero import logger


class ReliablySafeguardGuardian:
    def __init__(
        self,
        url: Union[str, Dict[str, str]],
        auth: Optional[Union[str, Dict[str, str]]],
        frequency: Optional[Union[float, Dict[str, str]]],
    ) -> None:
        self.guardian = safeguards.Guardian()

        url = get_value(url)  # type: ignore
        auth = get_value(auth)  # type: ignore

        if frequency is not None:
            frequency = max(float(get_value(frequency)), 0.3)  # type: ignore

        if not url:
            logger.debug("Missing URL for safeguard/precheck call")
            return None

        name = f"precheck-{sha256(url.encode()).hexdigest()}"  # type: ignore
        self.probes = [
            {
                "name": name,
                "type": "probe",
                "tolerance": True,
                "provider": {
                    "type": "python",
                    "module": "chaosreliably.activities.safeguard.probes",
                    "func": "call_endpoint",
                    "arguments": {"url": url, "auth": auth},
                },
            }
        ]

        if frequency:
            logger.debug(f"Will call '{url}' every {frequency}s as a safeguard")
            self.probes[0]["frequency"] = frequency
        else:
            logger.debug(f"Will call '{url}' once as a precheck")

        self.guardian.prepare(self.probes)

    def start(
        self,
        experiment: Experiment,
        configuration: Configuration,
        secrets: Secrets,
    ) -> None:
        self.guardian.run(
            experiment,
            self.probes,
            configuration or {},
            secrets or {},
            None,
        )

    def finish(self) -> None:
        self.guardian.terminate()


class ReliablySafeguardHandler(RunEventHandler):  # type: ignore
    def __init__(self) -> None:
        RunEventHandler.__init__(self)
        self._lock = threading.Lock()
        self._initialized = False
        self._started = False
        self.guardians = []  # type: ignore

    @property
    def initialized(self) -> bool:
        with self._lock:
            return self._initialized

    @initialized.setter
    def initialized(self, value: bool) -> None:
        with self._lock:
            self._initialized = value

    def register(self, event_registry: EventHandlerRegistry) -> None:
        with self._lock:
            if not self._initialized:
                event_registry.register(proxy)
                self._initialized = True

    def start_all(
        self,
        experiment: Experiment,
        configuration: Configuration,
        secrets: Secrets,
    ) -> None:
        if not self.initialized:
            return None

        with self._lock:
            if self._started:
                return None

            self._started = True

            for g in self.guardians:
                g.start(experiment, configuration, secrets)

    def finish(self, journal: Journal) -> None:
        if not self.initialized:
            return None

        with self._lock:
            guardians = self.guardians[:]
            self.guardians = []

        for g in guardians:
            g.finish()

    def add(self, guardian: ReliablySafeguardGuardian) -> None:
        if not self.initialized:
            return None

        with self._lock:
            self.guardians.append(guardian)


proxy = ReliablySafeguardHandler()


def initialize(
    event_registry: EventHandlerRegistry,
    handler: Optional[ReliablySafeguardHandler] = None,
) -> None:
    (handler or proxy).register(event_registry)


def register(
    url: Union[str, Dict[str, str]],
    auth: Optional[Union[str, Dict[str, str]]] = None,
    frequency: Optional[Union[float, Dict[str, str]]] = None,
    handler: Optional[ReliablySafeguardHandler] = None,
) -> None:
    (handler or proxy).add(ReliablySafeguardGuardian(url, auth, frequency))


def run_all(
    experiment: Experiment, configuration: Configuration, secrets: Secrets,
    handler: Optional[ReliablySafeguardHandler] = None,
) -> None:
    (handler or proxy).start_all(experiment, configuration, secrets)


def find_extension_by_name(
    experiment: Experiment, name: str
) -> Optional[Extension]:
    extensions = experiment.get("extensions")
    if not extensions:
        return None

    for extension in extensions:
        if extension["name"] == name:
            return cast(Extension, extension)

    return None


def get_value(value: Union[str, Dict[str, str]]) -> Optional[str]:
    if not value:
        return None

    if isinstance(value, str):
        return value

    if isinstance(value, float):
        return str(value)

    if value.get("type") == "env":
        return os.getenv(value["key"])

    return None
