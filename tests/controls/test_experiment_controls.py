from chaosreliably.controls import experiment


def test_experiment_controls_exposes_correct___all___values() -> None:
    assert [
        "before_experiment_control",
        "before_hypothesis_control",
    ] == experiment.__all__
