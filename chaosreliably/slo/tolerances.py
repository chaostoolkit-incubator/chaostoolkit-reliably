from typing import Dict, List

from logzero import logger
from tabulate import tabulate

__all__ = ["all_objective_results_ok"]


def all_objective_results_ok(value: List[Dict] = None) -> bool:
    """
    Determines if any of the objective results provided had a `remainingPercent` of less
    than 0. This means the SLO failed:
    Take a case where an objective is set at 99% and the actual percent is 90%, the
    remaining percent from the two is -9% and it has therefore failed.
    If an objective is set to 90% and the actual percent is 99% then the remaining
    percent is 9% and the SLO has passed.

    :param value: List[Dict] representing the Objective Results to check
    :returns: bool representing whether all the Objective Results were OK or not
    """
    not_ok_results = []

    for result in value:
        if result["spec"]["remainingPercent"] < 0:
            not_ok_results.append(
                [
                    result["metadata"]["labels"]["from"],
                    result["metadata"]["labels"]["to"],
                    result["spec"]["objectivePercent"],
                    result["spec"]["actualPercent"],
                    result["spec"]["remainingPercent"],
                    result["spec"]["indicatorSelector"],
                ]
            )

    if not_ok_results:
        headers = [
            "From",
            "To",
            "Objective %",
            "Actual %",
            "Remaining %",
            "Indicator Selector",
        ]
        logger.critical(
            "The following Objective Results were not OK:\n\n"
            "Objective Results are sorted by latest at the top:\n"
            f"{tabulate(not_ok_results, headers=headers, tablefmt='github')}"
        )
        return False
    else:
        logger.info("All Objective Results were OK.")
        return True
