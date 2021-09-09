from __future__ import annotations

from typing import Any, Dict, List

from pydantic import BaseModel, Field, parse_obj_as


class ApiObjectiveResultMetadata(BaseModel):
    labels: Dict[str, str]
    related_to: List[Dict[str, str]] = Field(alias="relatedTo", default=None)


class ApiObjectiveResultSpec(BaseModel):
    indicator_selector: Dict[str, str] = Field(alias="indicatorSelector")
    objective_percent: float = Field(alias="objectivePercent")
    actual_percent: float = Field(alias="actualPercent")
    remaining_percent: float = Field(alias="remainingPercent")


class ApiObjectiveResult(BaseModel):
    metadata: ApiObjectiveResultMetadata
    spec: ApiObjectiveResultSpec

    def parse_list(obj: Any) -> List[ApiObjectiveResult]:
        return parse_obj_as(List[ApiObjectiveResult], obj)
