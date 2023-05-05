import random
import re
from typing import Any, Dict, Optional, cast

import httpx
from chaoslib.exceptions import ActivityFailed
from chaoslib.types import Configuration, Secrets
from logzero import logger

from chaosreliably.activities.gh import get_gh_token, get_period

__all__ = ["cancel_workflow_run"]


def cancel_workflow_run(
    repo: str,
    at_random: bool = False,
    commit_message_pattern: Optional[str] = None,
    actor: Optional[str] = None,
    branch: str = "main",
    event: str = "push",
    status: str = "in_progress",
    window: str = "5d",
    exclude_pull_requests: bool = False,
    configuration: Configuration = None,
    secrets: Secrets = None,
) -> Dict[str, Any]:
    """
    Cancels a GitHub Workflow run.

    The target run is chosen from the list of workflow runs matching the
    given parameters.

    To refine the choice, you can set `commit_message_pattern` which is a
    regex matching the commit message that triggered the event.

    If you set `at_random`, a run will be picked from the matching list
    randomly. otherwise, the first match will be used.

    See the parameters meaning and values at:
    https://docs.github.com/en/rest/actions/workflow-runs?apiVersion=2022-11-28#list-workflow-runs-for-a-repository
    """
    gh_token = get_gh_token(secrets)
    start, _ = get_period(window)
    api_url = f"https://api.github.com/repos/{repo}/actions/runs"

    params = {
        "branch": branch,
        "event": event,
        "status": status,
        "created": ">" + start.strftime("%Y-%m-%d"),
        "exclude_pull_requests": exclude_pull_requests,
        "page": 1,
    }

    if actor:
        params["actor"] = actor

    r = httpx.get(
        api_url,
        headers={
            "accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "Authorization": f"Bearer {gh_token}",
        },
        params=params,  # type: ignore
    )

    if r.status_code > 399:
        logger.debug(f"failed to list runs for repo '{repo}': {r.json()}")
        raise ActivityFailed(f"failed to retrieve PR for repo '{repo}'")

    result = r.json()
    count = result["total_count"]

    logger.debug(f"Found {count} GitHub workflow runs that matched your query")

    target = None
    if count > 0:
        runs = result.get("workflow_runs", [])

        if commit_message_pattern is not None:
            pattern = re.compile(commit_message_pattern)

            for run in runs:
                m = run["head_commit"]["message"]
                if pattern:
                    if pattern.match(m) is not None:
                        target = run
                        break
        else:
            index = 0
            if at_random:
                index = random.randint(0, count - 1)
            target = runs[index]

    if not target:
        raise ActivityFailed(
            "Failed to locate a GitHub Worlflow run matching your query"
        )

    run_id = target["id"]
    api_url = f"{api_url}/{run_id}/cancel"

    r = httpx.post(
        api_url,
        headers={
            "accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "Authorization": f"Bearer {gh_token}",
        },
    )

    if r.status_code > 399:
        logger.debug(f"failed to cancel run {run_id} in '{repo}': {r.json()}")
        raise ActivityFailed(f"failed to cancel run {run_id} in '{repo}'")

    logger.debug(f"Cancelled workflow run {run_id}")

    return cast(Dict[str, Any], target)
