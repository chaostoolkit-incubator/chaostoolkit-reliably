from typing import Any, Dict, List

from pydantic import BaseModel, Field, parse_obj_as


class ObjectiveResultMetadata(BaseModel):
    labels: Dict[str, str]
    related_to: List[Dict[str, str]] = Field(alias="relatedTo", default=None)


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
