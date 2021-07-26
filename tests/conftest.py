import json
import os
from pathlib import Path

from pytest import fixture

TEST_DATA_DIR = os.path.join(Path(__file__).parent, "data")


@fixture
def objective_results():
    with open(os.path.join(TEST_DATA_DIR, "objective_results.json"), "r") as json_in:
        return json.load(json_in)
