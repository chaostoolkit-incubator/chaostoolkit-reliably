from typing import Any, Dict, Optional

import opentracing  # type: ignore
import ujson
from chaoslib.types import Configuration, Experiment, Journal, Secrets
from logzero import logger

from chaosreliably import get_session

__all__ = ["after_experiment_control"]


def after_experiment_control(
    context: Experiment,
    exp_id: str,
    org_id: str,
    state: Journal,
    configuration: Configuration = None,
    secrets: Secrets = None,
    **kwargs: Any,
) -> None:

    tracer = opentracing.global_tracer()
    scope = tracer.scope_manager.active
    span = scope.span if scope else None
    if span:
        span.set_tag("reliably-control", "started")

    try:
        complete_run(org_id, exp_id, context, state, configuration, secrets)
    except Exception as ex:
        logger.debug(
            f"An error occurred: {ex}, while running the after-experiment "
            "control, the execution won't be affected.",
            exc_info=True,
        )
    finally:
        if span:
            span.set_tag("reliably-control", "finished")


###############################################################################
# Private functions
###############################################################################
def complete_run(
    org_id: str,
    exp_id: str,
    experiment: Experiment,
    state: Journal,
    configuration: Configuration,
    secrets: Secrets,
) -> Optional[Dict[str, Any]]:
    with get_session(configuration, secrets) as session:
        resp = session.post(
            f"/{org_id}/experiments/{exp_id}/executions",
            json={"result": ujson.dumps(state)},
        )
        logger.debug(f"Response from {resp.url}: {resp.status_code}")
        if resp.status_code == 200:
            payload = resp.json()
            return payload  # type: ignore
    return None
