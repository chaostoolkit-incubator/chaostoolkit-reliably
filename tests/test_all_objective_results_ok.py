from chaosreliably.slo.tolerances import all_objective_results_ok


def test_all_objective_results_ok_when_results_all_ok(objective_results_all_ok):
    all_ok = all_objective_results_ok(objective_results_all_ok)
    assert all_ok


def test_all_objective_results_ok_when_results_not_all_ok(objective_results):
    all_ok = all_objective_results_ok(objective_results)
    assert not all_ok
