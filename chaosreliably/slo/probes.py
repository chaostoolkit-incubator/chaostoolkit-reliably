# -*- coding: utf-8 -*-
from collections import deque
from typing import Dict, List

import httpx
from chaoslib.exceptions import ActivityFailed
from chaoslib.types import Configuration, Secrets
from logzero import logger

from chaosreliably import get_session
from chaosreliably.slo.types import Reports

__all__ = ["get_slo_history", "get_last_N_slos"]


def get_last_N_slos(
    quantity: int = 5, configuration: Configuration = None, secrets: Secrets = None
) -> Dict[str, List[Dict]]:

    """
    Fetch the last N SLO reports in a structure that makes it easy to navigate
    them, for instance from a tolerance.
    """
    dataset = {}
    history = get_slo_history(configuration, secrets)

    reports = history.reports
    for report in reports:
        for service in report.services:
            for slo in service.service_levels:
                key = "{}/{}/{}".format(service.name, slo.type, slo.name)
                result = slo.result
                if result:
                    value = dataset.setdefault(key, deque([], quantity))
                    value.append(slo.dict())

    # mapping to lists as deque can not serialize nicely
    for key in dataset:
        dataset[key] = list(dataset[key])

    return dataset


##############################################################################
# Internal
##############################################################################
def get_slo_history(
    limit: int = 25, configuration: Configuration = None, secrets: Secrets = None
) -> Reports:
    """
    Fetch the history of SLO reports as provided by Reliably.
    """
    limit = min(limit or 25, 25)
    with get_session(configuration, secrets) as session:
        history = fetch_history(session, limit=limit)
        return history


def fetch_history(
    session: httpx.Client, limit: int = 25, cursor: str = None
) -> Reports:
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor

    url = f"{session.reliably_url}/reports/history"

    r = session.get(url=url, params=params)
    logger.debug("Fetched SLO history from: {}".format(r.url))
    if r.status_code != 200:
        raise ActivityFailed("Failed to retrieve SLO history: {}".format(r.text))

    history = r.json()

    return Reports.parse_obj(history)
