__all__ = ["response_time_must_be_under"]


def response_time_must_be_under(latency: float, value: float = 0.) -> bool:
    """
    Validates the response time is under the given latency.

    Use this as the tolerance of the
    `chaosreliably.activities.http.probes.measure_response_time` probe.
    """
    return value <= latency
