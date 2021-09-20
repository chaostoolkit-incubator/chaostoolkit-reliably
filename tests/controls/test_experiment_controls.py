from chaosreliably.controls import experiment


def test_experiment_controls_exposes_correct___all___values() -> None:
    for func in [
        "before_experiment_control",
        "before_hypothesis_control",
        "after_hypothesis_control",
        "before_method_control",
    ]:
        assert func in experiment.__all__
