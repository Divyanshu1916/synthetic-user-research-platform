from pydantic import BaseModel, Field
from typing import List


class Persona(BaseModel):
    name: str
    age: int
    education: str
    occupation: str

    personality_traits: List[str]
    behavioral_patterns: List[str]
    psychological_profile: List[str]

    goals: List[str]
    pain_points: List[str]
    preferred_features: List[str]

    price_sensitivity: str
    willingness_to_pay: str


class ResearchRequest(BaseModel):
    product_name: str
    product_description: str
    target_audience: str
    features: List[str]
    research_objective: str

    number_of_personas: int = Field(default=5, ge=1, le=20)

class PersonaList(BaseModel):
    personas: List[Persona]

class ReportRequest(BaseModel):
    product_name: str
    research_objective: str
    personas: List[Persona]
    survey_responses: list
    insights: str