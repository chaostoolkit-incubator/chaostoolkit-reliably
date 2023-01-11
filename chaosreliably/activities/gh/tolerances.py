import statistics
from typing import List, Optional

from logzero import logger

from chaosreliably import parse_duration

__all__ = ["ratio_under", "ratio_above", "percentile_under"]


def ratio_under(target: float, value: float = 0.0) -> bool:
    """
    Validates the ratio returned by a probe is strictly below the `target`.
    """
    logger.debug(f"Verify that ratio is below: {target}")
    return value < target


def ratio_above(target: float, value: float = 0.0) -> bool:
    """
    Validates the ratio returned by a probe is strictly greater than the
    `target`.
    """
    logger.debug(f"Verify that ratio is above: {target}")
    return value > target


def percentile_under(
    percentile: int,
    duration: str = "1d",
    value: Optional[List[int | float]] = None,
) -> bool:
    """
    Computes that the values under `percentile` are below the given duration.

    For instance, for PR durations, this could be helpful to understand that
    99% of them were closed in less than the given duration.
    """
    if not value:
        return True

    d = parse_duration(duration).total_seconds()
    q = statistics.quantiles(value, n=100)

    return q[percentile - 1] <= d
