import json
import os
from pathlib import Path

from pytest import fixture

TEST_DATA_DIR = os.path.join(Path(__file__).parent, "data")


@fixture
def objective_results():
    with open(os.path.join(TEST_DATA_DIR, "objective_results_from_api.json"), "r") as json_in:
        return json.load(json_in)


@fixture
def objective_results_all_ok(objective_results):
    for result in objective_results:
        result["spec"]["objectivePercent"] = 90.00
        result["spec"]["actualPercent"] = 100.00
        result["spec"]["remainingPercent"] = 0.00
    return objective_results
