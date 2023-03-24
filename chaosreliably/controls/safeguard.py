from typing import Any

from chaoslib.run import EventHandlerRegistry
from chaoslib.types import Configuration, Secrets
from logzero import logger

from . import ReliablySafeguardHandler

__all__ = ["configure_control"]


def configure_control(
    event_registry: EventHandlerRegistry,
    url: str,
    frequency: float,
    configuration: Configuration = None,
    secrets: Secrets = None,
    **kwargs: Any,
) -> None:
    logger.debug("Configure Reliably's safeguard control")

    event_registry.register(
        ReliablySafeguardHandler(url, frequency, configuration, secrets)
    )
