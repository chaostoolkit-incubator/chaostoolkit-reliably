# -*- coding: utf-8 -*-
from collections import deque
from typing import Dict, List
from urllib.parse import quote

import httpx
from chaoslib.exceptions import ActivityFailed
from chaoslib.types import Configuration, Secrets
from logzero import logger

from chaosreliably import get_session
from chaosreliably.slo.types import Reports

__all__ = ["get_slo_history", "get_last_N_slos", "get_objective_results_by_labels"]


def get_objective_results_by_labels(
    labels: Dict[str, str], configuration: Configuration = None, secrets: Secrets = None
) -> List[Dict]:
    """
    For a given set of Objective labels, return all of the Ojective Results
    """
    encoded_labels = quote(
        ",".join([f"{key}={value}" for key, value in labels.items()])
    )
    with get_session(configuration, secrets) as session:
        url = f"{session.reliably_url}/objectiveresult?objective-match={encoded_labels}"
        resp = session.get(url)
        logger.debug("Fetched SLO results from: {}".format(resp.url))
        if resp.status_code != 200:
            raise ActivityFailed("Failed to retrieve SLO results: {}".format(resp.text))
        return resp.json()
