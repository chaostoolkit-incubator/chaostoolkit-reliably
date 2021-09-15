from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional, Union
from uuid import uuid4

from pydantic import BaseModel as PydanticBaseModel
from pydantic import Field, parse_obj_as
from pydantic.networks import HttpUrl
from pydantic.types import UUID4

OPTIONAL_DICT_LIST = Optional[List[Dict[str, Any]]]
RELATED_TO = Field(alias="relatedTo", default=[])


class BaseModel(PydanticBaseModel):
    class Config:
        allow_population_by_field_name = True


class ObjectiveResultMetadata(BaseModel):
    labels: Dict[str, str]
    related_to: OPTIONAL_DICT_LIST = RELATED_TO


class ObjectiveResultSpec(BaseModel):
    indicator_selector: Dict[str, str] = Field(alias="indicatorSelector")
    objective_percent: float = Field(alias="objectivePercent")
    actual_percent: float = Field(alias="actualPercent")
    remaining_percent: float = Field(alias="remainingPercent")


class ObjectiveResult(BaseModel):
    metadata: ObjectiveResultMetadata
    spec: ObjectiveResultSpec

    def parse_list(obj: Any) -> "List[ObjectiveResult]":
        return parse_obj_as(List[ObjectiveResult], obj)


class ChaosToolkitType(Enum):
    EXPERIMENT: str = "Chaos Toolkit Experiment"
    EXPERIMENT_EVENT: str = "Chaos Toolkit Experiment Event"
    EXPERIMENT_RUN: str = "Chaos Toolkit Experiment Run"
    EXPERIMENT_VERSION: str = "Chaos Toolkit Experiment Version"


class EntityContextExperimentLabels(BaseModel):
    type: str = Field(
        default=ChaosToolkitType.EXPERIMENT.value, alias="_type", const=True
    )
    title: str = Field(alias="_experiment_title")


class EntityContextExperimentVersionLabels(BaseModel):
    type: str = Field(
        default=ChaosToolkitType.EXPERIMENT_VERSION.value, alias="_type", const=True
    )
    commit_hash: str = Field(alias="_commit_hash")
    source: HttpUrl = Field(alias="_source")


class EntityContextExperimentRunLabels(BaseModel):
    type: str = Field(
        default=ChaosToolkitType.EXPERIMENT_RUN.value, alias="_type", const=True
    )
    id: UUID4 = Field(default=uuid4(), alias="_run_id", const=True)
    timestamp: datetime = Field(
        alias="_run_timestamp",
        default=datetime.now(timezone.utc).isoformat(),
        const=True,
    )
    user: str = Field(alias="_run_user")


class EventType(Enum):
    EXPERIMENT_START = "EXPERIMENT_START"


class EntityContextExperimentEventLabels(BaseModel):
    type: str = Field(
        default=ChaosToolkitType.EXPERIMENT_EVENT.value, alias="_type", const=True
    )
    event_type: str = Field(alias="_event_type")
    timestamp: datetime = Field(
        alias="_event_timestamp",
        default=datetime.now(timezone.utc).isoformat(),
        const=True,
    )
    name: str = Field(alias="_event_name")
    output: Any = Field(alias="_event_output")


class EntityContextMetadata(BaseModel):
    labels: Union[
        EntityContextExperimentLabels,
        EntityContextExperimentVersionLabels,
        EntityContextExperimentRunLabels,
        EntityContextExperimentEventLabels,
    ]
    related_to: OPTIONAL_DICT_LIST = RELATED_TO


class EntityContext(BaseModel):
    metadata: EntityContextMetadata
