from typing import Any, cast

from chaoslib.types import Configuration, Experiment, Secrets
from logzero import logger

from chaosreliably import get_session
from chaosreliably.types import (
    EntityContext,
    EntityContextExperimentEventLabels,
    EntityContextExperimentLabels,
    EntityContextExperimentRunLabels,
    EntityContextExperimentVersionLabels,
    EntityContextMetadata,
    EventType,
)

__all__ = ["before_experiment_control"]


def before_experiment_control(
    context: Experiment,
    configuration: Configuration = None,
    secrets: Secrets = None,
    **kwargs: Any,
) -> None:
    """
    Control run *before* the execution of an Experiment.

    For a given Experiment, the control creates (if not already created) an Experiment
    Entity Context and an Experiment Version Entity Context in the Reliably Entity
    Server.

    A unique Experiment Run Entity Context is also created, with an Experiment Event
    Entity Context of type `EXPERIMENT_START` created, relating to the run.

    The control requires the `arguments` of `commit_hash`, `source`, and `user` to be
    provided to the control definition. If not provided, the control will simply not
    create any Entity Contexts.

    Once the Entity Contexts have been created, an entry into the configuration is made
    under configuration["chaosreliably"]["experiment_run_labels"] to allow for
    other controls to create events relating to the Experiment Run.

    :param context: Experiment object representing the Experiment that will be executed
    :param configuration: Configuration object provided by Chaos Toolkit
    :param secrets: Secret object provided by Chaos Toolkit
    :param **kwargs: Expected `kwargs` are 'commit_hash' (str), `source` (str), and
        `user` (str)

    Examples
    --------

    "controls": [
        {
            "name": "chaosreliably",
            "provider": {
                "type": "python",
                "module": "chaosreliably.controls"
                "arguments": {
                    "commit_hash": "59f9f577e2d90719098f4d23d26329ce41f2d0bd",
                    "source": "https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/exp.json",  # Noqa
                    "user": "A users name"
                }
            }
        }
    ]
    """
    try:
        commit_hash = kwargs.get("commit_hash")
        source = kwargs.get("source")
        user = kwargs.get("user")
        if not commit_hash or not source or not user:
            logger.warn(
                "The parameters: `commit_hash`, `source`, and `user` are required for "
                "the chaosreliably controls, please provide them. This Experiment Run"
                " will not be tracked with Reliably."
            )
            return

        experiment_run_labels = (
            _create_experiment_entities_for_before_experiment_control(
                experiment_title=context["title"],
                commit_hash=commit_hash,
                source=source,
                user=user,
                configuration=configuration,
                secrets=secrets,
            )
        )

        configuration.update(
            {"chaosreliably": {"experiment_run_labels": experiment_run_labels.dict()}}
        )
    except Exception as ex:
        logger.warn(
            f"An error occurred: {ex}, whilst running the Before Experiment control, "
            "no further entities will be created, the Experiment execution won't be "
            "affected"
        )


def _create_entity_context_on_reliably(
    entity_context: EntityContext, configuration: Configuration, secrets: Secrets
) -> EntityContext:
    """
    For a given EntityContext, create it on the Reliably Entity Server.

    :param entity_context: EntityContext which will be created on the Reliably Entity
        Server
    :param configuration: Configuration object provided by Chaos Toolkit
    :param secrets: Secret object provided by Chaos Toolkit
    :returns: EntityContext representing the EntityContext that was just created
    """
    with get_session(configuration, secrets) as session:
        url = "/entitycontext"
        resp = session.post(url, content=entity_context.json(by_alias=True))
        resp.raise_for_status()
        return entity_context


def _create_experiment(
    experiment_title: str, configuration: Configuration, secrets: Secrets
) -> EntityContextExperimentLabels:
    """
    For a given Experiment title, create a Experiment Entity Context
    on the Reliably Entity Server.

    :param experiment_title: str representing the name of the Experiment
    :param configuration: Configuration object provided by Chaos Toolkit
    :param secrets: Secret object provided by Chaos Toolkit
    :returns: EntityContextExperimentLabels representing the metadata labels of the
        created entity - used for `relatedTo` properties in Reliably
    """
    experiment_entity = EntityContext(
        metadata=EntityContextMetadata(
            labels=EntityContextExperimentLabels(title=experiment_title)
        )
    )

    created_entity = _create_entity_context_on_reliably(
        entity_context=experiment_entity, configuration=configuration, secrets=secrets
    )
    return cast(EntityContextExperimentLabels, created_entity.metadata.labels)


def _create_experiment_version(
    commit_hash: str,
    source: str,
    experiment_labels: EntityContextExperimentLabels,
    configuration: Configuration,
    secrets: Secrets,
) -> EntityContextExperimentVersionLabels:
    """
    For a given commit hash, source link, and Experiment labels, create a
    ExperimentVersion Entity Context on the Reliably Entity Server.

    :param commit_hash: str representing the SHA1 Hash of the current commit of the
        Experiments repo at the time of running it
    :param source: str representing the URL to the source control location
        of the Experiment being run
    :param experiment_labels: EntityContextExperimentLabels object representing the
        labels of the Experiment this version is related to
    :param configuration: Configuration object provided by Chaos Toolkit
    :param secrets: Secret object provided by Chaos Toolkit
    :returns: EntityContextExperimentVersionLabels representing the metadata labels
        of the created entity - used for `relatedTo` properties in Reliably
    """
    experiment_version_entity = EntityContext(
        metadata=EntityContextMetadata(
            labels=EntityContextExperimentVersionLabels(
                commit_hash=commit_hash,
                source=source,
            ),
            related_to=[experiment_labels],
        )
    )

    created_entity = _create_entity_context_on_reliably(
        entity_context=experiment_version_entity,
        configuration=configuration,
        secrets=secrets,
    )
    return cast(EntityContextExperimentVersionLabels, created_entity.metadata.labels)


def _create_experiment_run(
    user: str,
    experiment_version_labels: EntityContextExperimentVersionLabels,
    configuration: Configuration,
    secrets: Secrets,
) -> EntityContextExperimentRunLabels:
    """
    For a given user and Experiment Version labels, create a ExperimentRun Entity
    Context on the Reliably Entity Server.

    :param user: str representing the name of the user that is running the Experiment
    :param experiment_version_labels: EntityContextExperimentVersionLabels object
        representing the labels of the Experiment Version this run is related to
    :param configuration: Configuration object provided by Chaos Toolkit
    :param secrets: Secret object provided by Chaos Toolkit
    :returns: EntityContextExperimentRunLabels representing the metadata labels of
        the created entity - used for `relatedTo` properties in Reliably
    """
    experiment_run_entity = EntityContext(
        metadata=EntityContextMetadata(
            labels=EntityContextExperimentRunLabels(user=user),
            related_to=[experiment_version_labels],
        )
    )

    created_entity = _create_entity_context_on_reliably(
        entity_context=experiment_run_entity,
        configuration=configuration,
        secrets=secrets,
    )
    return cast(EntityContextExperimentRunLabels, created_entity.metadata.labels)


def _create_experiment_event(
    event_type: EventType,
    name: str,
    output: Any,
    experiment_run_labels: EntityContextExperimentRunLabels,
    configuration: Configuration,
    secrets: Secrets,
) -> EntityContextExperimentEventLabels:
    """
    For a given event type, name, output, and Experiment Run labels, create a
    ExperimentEvent Entity Context on the Reliably Entity Server.

    :param event_type: EventType representing the type of the Event that has happened
    :param name: str representing the name of the Event in the Experiment
    :param output: Any object representing the output of the event in the Experiment
    :param experiment_run_labels: EntityContextExperimentRunLabels object
        representing the labels of the Experiment Run this Event is related to
    :param configuration: Configuration object provided by Chaos Toolkit
    :param secrets: Secret object provided by Chaos Toolkit
    :returns: EntityContextExperimentEventLabels representing the metadata labels of
        the created entity - used for `relatedTo` properties in Reliably
    """
    experiment_event_entity = EntityContext(
        metadata=EntityContextMetadata(
            labels=EntityContextExperimentEventLabels(
                event_type=event_type.value, name=name, output=output
            ),
            related_to=[experiment_run_labels],
        )
    )

    created_entity = _create_entity_context_on_reliably(
        entity_context=experiment_event_entity,
        configuration=configuration,
        secrets=secrets,
    )
    return cast(EntityContextExperimentEventLabels, created_entity.metadata.labels)


def _create_experiment_entities_for_before_experiment_control(
    experiment_title: str,
    commit_hash: str,
    source: str,
    user: str,
    configuration: Configuration,
    secrets: Secrets,
) -> EntityContextExperimentRunLabels:
    """
    For a given Experiment title, commit hash, source link and user, create
    an Experiment, Experiment Version, Experiment Run, and Experiment start Entity
    Context on the Reliably Entity Server.

    If the Experiment and version already exist, new ones will not be created, however
    a new run is *always* created.

    :param experiment_title: str representing the name of the Experiment
    :param commit_hash: str representing the SHA1 Hash of the current commit of the
        Experiments repo at the time of running it
    :param source: str representing the URL to the source control location
        of the Experiment being run
    :param user: str representing the name of the user that is running the Experiment
    :param configuration: Configuration object provided by Chaos Toolkit
    :param secrets: Secret object provided by Chaos Toolkit
    :returns: EntityContextExperimentRunLabels representing the metadata labels of
        the Experiment Run entity - used for updating the configuration of the
        Experiment so that Events may relate to it
    """
    experiment_labels = _create_experiment(
        experiment_title=experiment_title, configuration=configuration, secrets=secrets
    )
    experiment_version_labels = _create_experiment_version(
        commit_hash=commit_hash,
        source=source,
        experiment_labels=experiment_labels,
        configuration=configuration,
        secrets=secrets,
    )
    experiment_run_labels = _create_experiment_run(
        user=user,
        experiment_version_labels=experiment_version_labels,
        configuration=configuration,
        secrets=secrets,
    )
    _ = _create_experiment_event(
        event_type=EventType.EXPERIMENT_START,
        name=f"Experiment: {experiment_title} - Started",
        output=None,
        experiment_run_labels=experiment_run_labels,
        configuration=configuration,
        secrets=secrets,
    )
    return experiment_run_labels