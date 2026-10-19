from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from models import ResearchRequest
from agent import generate_personas
from database import save_persona
from survey import conduct_survey
from insights import extract_insights


class ResearchState(TypedDict):
    product_name: str
    product_description: str
    target_audience: str
    features: list[str]
    research_objective: str
    number_of_personas: int
    personas: list
    survey_responses: list
    insights: str


def start_research(state: ResearchState):
    print("Starting synthetic user research...")

    return state


def generate_synthetic_personas(state: ResearchState):
    print("Generating synthetic personas...")

    request = ResearchRequest(
        product_name=state["product_name"],
        product_description=state["product_description"],
        target_audience=state["target_audience"],
        features=state["features"],
        research_objective=state["research_objective"],
        number_of_personas=state["number_of_personas"]
    )

    result = generate_personas(request)

    for persona in result.personas:
        save_persona(persona)

    print("Personas saved to database.")

    return {
        "personas": result.personas
    }


def conduct_synthetic_survey(state: ResearchState):
    print("Conducting synthetic survey...")

    personas = state["personas"]

    question = (
        "Would you pay ₹99 per month for this Smart Student Planner? "
        "Why or why not?"
    )

    responses = conduct_survey(
        personas,
        question
    )

    print("Survey completed.")

    return {
        "survey_responses": responses
    }


def extract_research_insights(state: ResearchState):
    print("Extracting research insights...")

    survey_responses = state.get("survey_responses", [])

    if not survey_responses:
        print("No survey responses available.")

        return {
            "insights": ""
        }

    insights = extract_insights(
        product_name=state["product_name"],
        research_objective=state["research_objective"],
        survey_responses=survey_responses
    )

    print("Research insights extracted.")

    return {
        "insights": insights
    }


builder = StateGraph(ResearchState)

builder.add_node("start_research", start_research)
builder.add_node("generate_personas", generate_synthetic_personas)
builder.add_node("conduct_survey", conduct_synthetic_survey)
builder.add_node("extract_insights", extract_research_insights)

builder.add_edge(START, "start_research")
builder.add_edge("start_research", "generate_personas")
builder.add_edge("generate_personas", "conduct_survey")
builder.add_edge("conduct_survey", "extract_insights")
builder.add_edge("extract_insights", END)

research_graph = builder.compile()