import os
from typing import Optional

from chaoslib.types import Configuration, Experiment, Journal, Secrets

__all__ = ["OTELVendorHandler"]


class OTELVendorHandler:
    @staticmethod
    def is_on() -> bool:
        try:
            from opentelemetry import baggage  # noqa: F401
        except ImportError:
            return False

        return os.getenv("OTEL_EXPORTER_OTLP_TRACES_HEADERS") is not None

    def started(
        self,
        experiment: Experiment,
        plan_id: Optional[str],
        execution_id: str,
        execution_url: str,
        configuration: Configuration,
        secrets: Secrets,
    ) -> None:
        from opentelemetry import baggage

        baggage.set_baggage("reliably.experiment.name", experiment["title"])
        baggage.set_baggage("reliably.execution.id", execution_id)
        baggage.set_baggage("reliably.execution.url", execution_url)
        baggage.set_baggage("reliably.plan.id", plan_id)

    def finished(
        self, journal: Journal, configuration: Configuration, secrets: Secrets
    ) -> None:
        from opentelemetry import baggage

        baggage.set_baggage("reliably.execution.status", journal["status"])
        baggage.set_baggage(
            "reliably.execution.deviated", str(journal["deviated"])
        )
