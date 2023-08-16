from typing import Any, Dict, Optional

from chaoslib.types import Configuration, Experiment, Secrets
from logzero import logger

from chaosreliably.controls.capture import slack


def get_control_by_name(
    name: str, experiment: Experiment
) -> Optional[Dict[str, Any]]:
    ctrls = experiment.get("controls")
    if not ctrls:
        return None

    for ctrl in ctrls:
        if ctrl["name"] == name:
            return ctrl

    return None


def start_capturing(
    experiment: Experiment, configuration: Configuration, secrets: Secrets
) -> None:
    try:
        slack.start_capturing(experiment, configuration, secrets)
    except Exception:
        logger.debug("Failed to start capturing slack messages", exc_info=True)


def stop_capturing(
    experiment: Experiment, configuration: Configuration, secrets: Secrets
) -> Optional[Dict[str, Any]]:
    slack_cap = None

    try:
        slack_cap = slack.stop_capturing(experiment, configuration, secrets)
    except Exception:
        logger.debug("Failed to stop capturing slack messages", exc_info=True)

    captures = {"slack": slack_cap}

    return captures