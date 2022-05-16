from unittest.mock import MagicMock, patch

from chaosreliably.controls import experiment
from chaosreliably.types import EventType


@patch("chaosreliably.controls.experiment.create_run_event")
def test_before_hypothesis_control_calls_create_run_event(
    mock_create_run_event: MagicMock,
) -> None:
    configuration = {"chaosreliably": {"run_ref": "run-123"}}
    context = {}  # type: ignore
    x = {}  # type: ignore

    experiment.before_hypothesis_control(
        context=context,
        experiment=x,
        experiment_ref="XYZ",
        configuration=configuration,
        secrets=None,
    )

    mock_create_run_event.assert_called_once_with(
        "XYZ",
        "run-123",
        event_type=EventType.HYPOTHESIS_START,
        experiment=x,
        output=None,
        experiment_run_labels={"experiment_run_ref": "run-123"},
        configuration=configuration,
        secrets=None,
    )


@patch("chaosreliably.controls.experiment.logger")
@patch("chaosreliably.controls.experiment.create_run_event", autospec=True)
def test_that_an_exception_does_not_get_raised_and_warning_logged(
    mock_create_run_event: MagicMock,
    mock_logger: MagicMock,
) -> None:
    configuration = {"chaosreliably": {"run_ref": "run-123"}}
    context = {}  # type: ignore
    x = {}  # type: ignore

    mock_create_run_event.side_effect = Exception("'chaosreliably'")
    experiment.before_hypothesis_control(
        context=context,
        experiment=x,
        experiment_ref="XYZ",
        configuration=configuration,
        secrets=None,
    )

    mock_logger.debug.assert_called_once_with(
        "An error occurred: 'chaosreliably', while running the Before "
        "Hypothesis control, the Experiment execution won't be affected.",
        exc_info=True,
    )
