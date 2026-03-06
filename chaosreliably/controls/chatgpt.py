import logging
import os
import threading
import time
from typing import Dict, Union

import httpx
import orjson
from chaoslib.run import EventHandlerRegistry, RunEventHandler
from chaoslib.types import (
    Configuration,
    Experiment,
    Journal,
    Schedule,
    Secrets,
    Settings,
)

from chaosreliably.controls import find_extension_by_name, global_lock

__all__ = ["configure_control"]
logger = logging.getLogger("chaostoolkit")
OPENAI_URL = "https://api.openai.com/v1/chat/completions"


class OpenAIHandler(RunEventHandler):  # type: ignore
    def __init__(
        self,
        openai_model: Union[str, Dict[str, str]],
    ) -> None:
        RunEventHandler.__init__(self)
        self.openai_model = openai_model
        self.should_exit = threading.Event()
        self.allow_journal_review = False
        self.secrets = None
        self._t = None

    def running(
        self,
        experiment: Experiment,
        journal: Journal,
        configuration: Configuration,
        secrets: Secrets,
        schedule: Schedule,
        settings: Settings,
    ) -> None:
        extension = find_extension_by_name(experiment, "chatgpt")
        if not extension:
            logger.warning(
                "OpenAI extension will not do anything. We need at least one user prompt."
            )
            return None

        self.allow_journal_review = extension.get("allow_journal_review", False)
        if self.allow_journal_review:
            self.secrets = secrets.copy()

        logger.debug("Starting OpenAI GPT conversation in background")
        self._t = threading.Thread(  # type: ignore
            None,
            talk_with_chatgpt,
            kwargs=dict(
                state=journal,
                openai_model=self.openai_model,
                should_exit=self.should_exit,
                secrets=secrets,
            ),
            daemon=True,
        )
        self._t.start()  # type: ignore

    def finish(self, journal: Journal) -> None:
        if self.allow_journal_review:
            logger.debug("Review journal with LLM...")
            review_journal(
                journal, openai_model=self.openai_model, secrets=self.secrets
            )
            self.secrets = None

        if self._t is not None and self._t.is_alive():
            try:
                global_lock.acquire()
                self.should_exit.set()
                logger.debug(
                    "Waiting for OpenAI GPT conversation to finish "
                    "(for up to 90s)"
                )
                self._t.join(timeout=95)
            except RuntimeError:
                logger.debug(
                    "Failure while waiting for OpenAI to finish", exc_info=True
                )
            finally:
                logger.debug("Finished conversing with ChatGPT")
                global_lock.release()
                self._t = None


def configure_control(
    openai_model: Union[str, Dict[str, str]],
    event_registry: EventHandlerRegistry,
    configuration: Configuration = None,
    secrets: Secrets = None,
    settings: Settings = None,
    experiment: Experiment = None,
) -> None:
    event_registry.register(OpenAIHandler(openai_model))


###############################################################################
# Private functions
###############################################################################
SYSTEM_PROMPTS = [
    {
        "role": "system",
        "content": "You are a helpful assistant for DevOps or SRE engineering team trying to improve their reliability and resilience through Chaos Engineering. This is not an interactive chat. You must contain your comprehensive answer in that one response.",
    },
    {
        "role": "system",
        "content": "You aware of the Reliably & Chaos Toolkit and understand the responses may be useful in context of Chaos Toolkit experiments.",
    },
    {
        "role": "system",
        "content": "You respond in unrendered markdown format and do not prefix the response with ```markdown",
    },
]


def talk_with_chatgpt(
    state: Journal,
    should_exit: threading.Event,
    openai_model: Union[str, Dict[str, str]] = "gpt-5-nano",
    secrets: Secrets = None,
) -> None:
    try:
        experiment = state["experiment"]
        extension = find_extension_by_name(experiment, "chatgpt")
        if not extension:
            return None

        if isinstance(openai_model, dict):
            openai_model = os.getenv(
                openai_model["key"],
                openai_model.get("default", "gpt-5-nano"),
            )

        secrets = secrets or {}
        openapi_secrets = secrets.get("openai", {})

        org = openapi_secrets.get("org") or os.getenv("OPENAI_ORG")
        if not org:
            logger.warning("Cannot call OpenAI: missing org")
            return None

        key = openapi_secrets.get("key") or os.getenv("OPENAI_API_KEY")
        if not key:
            logger.warning("Cannot call OpenAI: missing secret key")
            return None

        logger.debug(
            f"Asking OpenAPI for chat completions using model '{openai_model}'"
        )

        start = time.time()
        backoff = 3
        results = []
        chat = SYSTEM_PROMPTS[:]
        for message in extension.get("messages", [])[:]:
            if should_exit.is_set():
                logger.debug("Exiting OpenAI chat as experiment has finished")
                break

            chat.append(message)

            try:
                logger.debug("Submitting message to OpenAI")
                r = httpx.post(
                    OPENAI_URL,
                    timeout=90,
                    headers={
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {key}",
                        "OpenAI-Organization": org,
                    },
                    json={"model": openai_model, "messages": chat},
                )
            except httpx.ReadTimeout:
                logger.debug("OpenAI took too long to respond unfortunately")
            else:
                if r.status_code == 429:
                    logger.debug(
                        f"OpenAI models overloaded. Pausing {backoff}s before "
                        "continuing communicating with OpenAI again."
                    )
                    time.sleep(backoff)
                    backoff += 2
                elif r.status_code > 399:
                    logger.debug(
                        f"OpenAI chat failed: {r.status_code}: {r.json()}"
                    )
                else:
                    results.append(r.json())
                    chat.append(results[-1]["choices"][0]["message"])
                    logger.debug("Got a reply from OpenAI")

        d = time.time() - start
        logger.debug(f"Finished fetching OpenAI messages in {d}s")
        extension["results"] = results
    except Exception:
        logger.debug("Failure to communicate with OpenAI API", exc_info=True)


def review_journal(
    state: Journal,
    openai_model: Union[str, Dict[str, str]] = "gpt-5-nano",
    secrets: Secrets = None,
) -> None:
    experiment = state["experiment"]
    extension = find_extension_by_name(experiment, "chatgpt")
    if not extension:
        return None

    results = extension["results"]

    if isinstance(openai_model, dict):
        openai_model = os.getenv(
            openai_model["key"],
            openai_model.get("default", "gpt-5-nano"),
        )

    secrets = secrets or {}
    openapi_secrets = secrets.get("openai", {})

    org = openapi_secrets.get("org") or os.getenv("OPENAI_ORG")
    if not org:
        logger.warning("Cannot call OpenAI: missing org")
        return None

    key = openapi_secrets.get("key") or os.getenv("OPENAI_API_KEY")
    if not key:
        logger.warning("Cannot call OpenAI: missing secret key")
        return None

    logger.debug(
        f"Asking OpenAPI to review journal using model '{openai_model}'"
    )

    review_message = "Below is the full JSON journal of a Chaos Toolkit experiment's run. Please review it and provide sound and actionable remarks about the system's state."
    serialized_journal = orjson.dumps(state).decode("utf-8")
    review_message_with_payload = f"{review_message}\n\n{serialized_journal}\n"

    try:
        logger.debug("Submitting journal to OpenAI")
        chat = SYSTEM_PROMPTS[:]
        chat.append(
            {
                "role": "user",
                "content": review_message_with_payload,
            }
        )

        r = httpx.post(
            OPENAI_URL,
            timeout=90,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {key}",
                "OpenAI-Organization": org,
            },
            json={"model": openai_model, "messages": chat},
        )
    except httpx.ReadTimeout:
        logger.debug("OpenAI took too long to respond unfortunately")
    else:
        if r.status_code == 429:
            logger.debug("OpenAI models overloaded. Skipping execution review.")
        elif r.status_code > 399:
            logger.debug(f"OpenAI chat failed: {r.status_code}: {r.json()}")
        else:
            logger.debug("Finished reviewing journal")
            extension.get("messages", []).append(
                {
                    "role": "user",
                    "content": "Execution's review and feedback.",
                }
            )
            results.append(r.json())
            extension["results"] = results
