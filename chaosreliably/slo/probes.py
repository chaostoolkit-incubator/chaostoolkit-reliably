# -*- coding: utf-8 -*-
from typing import Dict, List
from urllib.parse import quote

from chaoslib.exceptions import ActivityFailed
from chaoslib.types import Configuration, Secrets
from logzero import logger

from chaosreliably import get_session

__all__ = ["get_objective_results_by_labels"]


def get_objective_results_by_labels(
    labels: Dict[str, str],
    limit: int = 1,
    configuration: Configuration = None,
    secrets: Secrets = None,
) -> List[Dict]:
    """
    For a given set of Objective labels, return all of the Ojective Results

    :param labels: Dict[str, str] representing the Objective Labels for the Objective
        to retrieve results for
    :param limit: int representing how many results to retrieve - Default 1
    :param configuration: Configuration object provided by Chaos Toolkit
    :param secrets: Secret object provided by Chaos Toolkit
    :returns: List[Dict] representing the Objective Results for the given Objective

    """
    encoded_labels = quote(
        ",".join([f"{key}={value}" for key, value in labels.items()])
    )
    with get_session(configuration, secrets) as session:
        url = f"{session.reliably_url}/objectiveresult?objective-match={encoded_labels}"
        resp = session.get(url, params={"limit": limit})
        logger.debug("Fetched SLO results from: {}".format(resp.url))
        if resp.status_code != 200:
            raise ActivityFailed("Failed to retrieve SLO results: {}".format(resp.text))
        return resp.json()
