from tempfile import NamedTemporaryFile
from typing import Any, Dict, cast
from unittest.mock import MagicMock, patch

import pytest
import pytest_httpx
import yaml
from httpx._exceptions import HTTPStatusError

from chaosreliably.controls import experiment
from chaosreliably.types import (
    EntityContext,
    EntityContextExperimentEventLabels,
    EntityContextExperimentLabels,
    EntityContextExperimentRunLabels,
    EntityContextExperimentVersionLabels,
    EntityContextMetadata,
    EventType,
)


def test_experiment_controls_exposes_correct___all___values() -> None:
    assert "before_experiment_control" in experiment.__all__


def test_create_entity_context_on_reliably_correctly_calls_reliably_api(
    httpx_mock: pytest_httpx._httpx_mock.HTTPXMock,
) -> None:
    title = "A Test Experiment Title"
    request_url = "https://reliably.com/entities/test-org/reliably.com/v1/entitycontext"
    expected_entity = EntityContext(
        metadata=EntityContextMetadata(
            labels=EntityContextExperimentLabels(title=title),
        )
    )
    httpx_mock.add_response(
        method="POST",
        url=request_url,
        match_content=expected_entity.json(by_alias=True).encode("utf-8"),
    )
    with NamedTemporaryFile(mode="w") as f:
        yaml.safe_dump(
            {
                "auths": {"reliably.com": {"token": "12345", "username": "jane"}},
                "currentOrg": {"name": "test-org"},
            },
            f,
            indent=2,
            default_flow_style=False,
        )
        f.seek(0)

        entity_context = experiment._create_entity_context_on_reliably(
            entity_context=expected_entity,
            configuration={"reliably_config_path": f.name},
            secrets=None,
        )
        assert entity_context == expected_entity


def test_create_entity_context_on_reliably_raises_exception_if_response_not_ok(
    httpx_mock: pytest_httpx._httpx_mock.HTTPXMock,
) -> None:
    title = "A Test Experiment Title"
    request_url = "https://reliably.com/entities/test-org/reliably.com/v1/entitycontext"
    expected_entity = EntityContext(
        metadata=EntityContextMetadata(
            labels=EntityContextExperimentLabels(title=title),
        )
    )
    httpx_mock.add_response(
        method="POST",
        url=request_url,
        match_content=expected_entity.json(by_alias=True).encode("utf-8"),
        status_code=500,
    )
    with NamedTemporaryFile(mode="w") as f:
        yaml.safe_dump(
            {
                "auths": {"reliably.com": {"token": "12345", "username": "jane"}},
                "currentOrg": {"name": "test-org"},
            },
            f,
            indent=2,
            default_flow_style=False,
        )
        f.seek(0)

        with pytest.raises(HTTPStatusError):
            _ = experiment._create_entity_context_on_reliably(
                entity_context=expected_entity,
                configuration={"reliably_config_path": f.name},
                secrets=None,
            )


@patch("chaosreliably.controls.experiment._create_entity_context_on_reliably")
def test_create_experiment_correct_calls_create_entity_context_and_returns_labels(
    mock_create_entity_context: MagicMock,
) -> None:
    title = "A Test Experiment Title"
    experiment_context = EntityContext(
        metadata=EntityContextMetadata(
            labels=EntityContextExperimentLabels(title=title),
        )
    )
    mock_create_entity_context.return_value = experiment_context

    labels = experiment._create_experiment(
        experiment_title=title, configuration=None, secrets=None
    )

    assert labels == experiment_context.metadata.labels
    mock_create_entity_context.assert_called_once_with(
        entity_context=experiment_context, configuration=None, secrets=None
    )


@patch("chaosreliably.controls.experiment._create_entity_context_on_reliably")
def test_create_experiment_version_calls_create_entity_context_and_returns_labels(
    mock_create_entity_context: MagicMock,
) -> None:
    commit_hash = "59f9f577e2d90719098f4d23d26329ce41f2d0bd"
    source = "https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/exp.json"
    experiment_context = EntityContext(
        metadata=EntityContextMetadata(
            labels=EntityContextExperimentLabels(title="A Test Experiment Title"),
        )
    )
    experiment_version_context = EntityContext(
        metadata=EntityContextMetadata(
            labels=EntityContextExperimentVersionLabels(
                commit_hash=commit_hash, source=source
            ),
            related_to=[experiment_context.metadata.labels],
        )
    )
    mock_create_entity_context.return_value = experiment_version_context

    labels = experiment._create_experiment_version(
        commit_hash=commit_hash,
        source=source,
        experiment_labels=cast(
            EntityContextExperimentLabels, experiment_context.metadata.labels
        ),
        configuration=None,
        secrets=None,
    )

    assert labels == experiment_version_context.metadata.labels
    mock_create_entity_context.assert_called_once_with(
        entity_context=experiment_version_context, configuration=None, secrets=None
    )


@patch("chaosreliably.controls.experiment._create_entity_context_on_reliably")
def test_create_experiment_run_calls_create_entity_context_and_returns_labels(
    mock_create_entity_context: MagicMock,
) -> None:
    user = "TestUser"
    experiment_version_context = EntityContext(
        metadata=EntityContextMetadata(
            labels=EntityContextExperimentVersionLabels(
                commit_hash="59f9f577e2d90719098f4d23d26329ce41f2d0bd",
                source="https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/exp.json",  # noqa
            )
        )
    )
    experiment_run_context = EntityContext(
        metadata=EntityContextMetadata(
            labels=EntityContextExperimentRunLabels(user=user),
            related_to=[experiment_version_context.metadata.labels],
        )
    )
    mock_create_entity_context.return_value = experiment_run_context

    labels = experiment._create_experiment_run(
        user=user,
        experiment_version_labels=cast(
            EntityContextExperimentVersionLabels,
            experiment_version_context.metadata.labels,
        ),
        configuration=None,
        secrets=None,
    )

    assert labels == experiment_run_context.metadata.labels
    mock_create_entity_context.assert_called_once_with(
        entity_context=experiment_run_context, configuration=None, secrets=None
    )


@patch("chaosreliably.controls.experiment._create_entity_context_on_reliably")
def test_create_experiment_event_calls_create_entity_context_and_returns_labels(
    mock_create_entity_context: MagicMock,
) -> None:
    event_type = EventType.EXPERIMENT_START
    event_name = "A Start Event"
    event_output = [1, 2, 3]
    experiment_run_context = EntityContext(
        metadata=EntityContextMetadata(
            labels=EntityContextExperimentRunLabels(user="TestUser"),
        )
    )
    experiment_event_context = EntityContext(
        metadata=EntityContextMetadata(
            labels=EntityContextExperimentEventLabels(
                event_type=event_type.value, name=event_name, output=event_output
            ),
            related_to=[experiment_run_context.metadata.labels],
        )
    )
    mock_create_entity_context.return_value = experiment_event_context

    labels = experiment._create_experiment_event(
        event_type=event_type,
        name=event_name,
        output=event_output,
        experiment_run_labels=cast(
            EntityContextExperimentRunLabels, experiment_run_context.metadata.labels
        ),
        configuration=None,
        secrets=None,
    )

    assert labels == experiment_event_context.metadata.labels
    mock_create_entity_context.assert_called_once_with(
        entity_context=experiment_event_context, configuration=None, secrets=None
    )


@patch("chaosreliably.controls.experiment._create_experiment_event")
@patch("chaosreliably.controls.experiment._create_experiment_run")
@patch("chaosreliably.controls.experiment._create_experiment_version")
@patch("chaosreliably.controls.experiment._create_experiment")
def test_that_create_experiment_entities_for_before_experiment_control_creates_entities(
    mock_create_experiment: MagicMock,
    mock_create_experiment_version: MagicMock,
    mock_create_experiment_run: MagicMock,
    mock_create_experiment_event: MagicMock,
) -> None:
    title = "A title"
    commit_hash = "59f9f577e2d90719098f4d23d26329ce41f2d0bd"
    source = "https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/exp.json"
    user = "TestUser"
    name = f"Experiment: {title} - Started"
    experiment_context = EntityContext(
        metadata=EntityContextMetadata(
            labels=EntityContextExperimentLabels(title=title),
        )
    )
    experiment_version_context = EntityContext(
        metadata=EntityContextMetadata(
            labels=EntityContextExperimentVersionLabels(
                commit_hash=commit_hash,
                source=source,
            ),
            related_to=[experiment_context.metadata.labels],
        )
    )
    experiment_run_context = EntityContext(
        metadata=EntityContextMetadata(
            labels=EntityContextExperimentRunLabels(user=user),
            related_to=[experiment_version_context.metadata.labels],
        )
    )
    experiment_event_context = EntityContext(
        metadata=EntityContextMetadata(
            labels=EntityContextExperimentEventLabels(
                event_type=EventType.EXPERIMENT_START.value,
                name=name,
                output=None,
            ),
            related_to=[experiment_run_context.metadata.labels],
        )
    )
    mock_create_experiment.return_value = experiment_context.metadata.labels
    mock_create_experiment_version.return_value = (
        experiment_version_context.metadata.labels
    )
    mock_create_experiment_run.return_value = experiment_run_context.metadata.labels
    mock_create_experiment_event.return_value = experiment_event_context.metadata.labels

    experiment_run_labels = (
        experiment._create_experiment_entities_for_before_experiment_control(
            experiment_title=title,
            commit_hash=commit_hash,
            source=source,
            user=user,
            configuration=None,
            secrets=None,
        )
    )

    assert experiment_run_labels == experiment_run_context.metadata.labels

    mock_create_experiment.assert_called_once_with(
        experiment_title=title, configuration=None, secrets=None
    )
    mock_create_experiment_version.assert_called_once_with(
        commit_hash=commit_hash,
        source=source,
        experiment_labels=experiment_context.metadata.labels,
        configuration=None,
        secrets=None,
    )
    mock_create_experiment_run.assert_called_once_with(
        user=user,
        experiment_version_labels=experiment_version_context.metadata.labels,
        configuration=None,
        secrets=None,
    )
    mock_create_experiment_event.assert_called_once_with(
        event_type=EventType.EXPERIMENT_START,
        name=name,
        output=None,
        experiment_run_labels=experiment_run_context.metadata.labels,
        configuration=None,
        secrets=None,
    )


@patch(
    "chaosreliably.controls.experiment._create_experiment_entities_for_before_experiment_control"  # Noqa
)
def test_before_experiment_control_calls_create_experiment_entities(
    mock_create_experiment_entities: MagicMock,
) -> None:
    configuration = {"random_config": {"hi": "hello"}, "thing": 123}
    title = "A title"
    commit_hash = "59f9f577e2d90719098f4d23d26329ce41f2d0bd"
    source = "https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/exp.json"
    user = "TestUser"
    experiment_run_context = EntityContext(
        metadata=EntityContextMetadata(
            labels=EntityContextExperimentRunLabels(user="a-user")
        )
    )
    mock_create_experiment_entities.return_value = (
        experiment_run_context.metadata.labels
    )

    experiment.before_experiment_control(
        context={"title": title},
        configuration=configuration,
        secrets=None,
        commit_hash=commit_hash,
        source=source,
        user=user,
    )

    mock_create_experiment_entities.assert_called_once_with(
        experiment_title=title,
        commit_hash=commit_hash,
        source=source,
        user=user,
        configuration=configuration,
        secrets=None,
    )

    assert "chaosreliably" in configuration
    chaosreliably = cast(Dict[str, Any], configuration["chaosreliably"])
    assert (
        chaosreliably["experiment_run_labels"] == experiment_run_context.metadata.labels
    )


@patch("chaosreliably.controls.experiment.logger")
@patch(
    "chaosreliably.controls.experiment._create_experiment_entities_for_before_experiment_control"  # Noqa
)
def test_that_before_experiment_control_does_nothing_if_kwargs_not_present(
    mock_create_experiment_entities: MagicMock,
    mock_logger: MagicMock,
) -> None:
    experiment.before_experiment_control(
        context={"title": "a-title"},
        configuration=None,
        secrets=None,
    )
    mock_logger.warn.assert_called_once_with(
        "The parameters: `commit_hash`, `source`, and `user` are required for the "
        "chaosreliably controls, please provide them. This Experiment Run will not "
        "be tracked with Reliably."
    )
    mock_create_experiment_entities.assert_not_called()


@patch("chaosreliably.controls.experiment.logger")
@patch(
    "chaosreliably.controls.experiment._create_experiment_entities_for_before_experiment_control"  # Noqa
)
def test_that_an_exception_does_not_get_raised_and_warning_logged(
    mock_create_experiment_entities: MagicMock, mock_logger: MagicMock
) -> None:
    mock_create_experiment_entities.side_effect = Exception("An exception happened")
    experiment.before_experiment_control(
        context={"title": "a-title"},
        configuration=None,
        secrets=None,
        commit_hash="blah",
        source="blah",
        user="blah",
    )
    mock_logger.warn.assert_called_once_with(
        "An error occurred: An exception happened, whilst running the Before Experiment"
        " control, no further entities will be created, the Experiment execution won't"
        " be affected"
    )
