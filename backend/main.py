from fastapi import FastAPI

from models import ResearchRequest, Persona, ReportRequest
from graph import research_graph
from survey import conduct_survey
from interview import conduct_interview
from insights import extract_insights
from report import generate_report


app = FastAPI(
    title="Synthetic User Research Platform",
    description="AI-powered synthetic user research backend",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Synthetic User Research Platform API is running"
    } 


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/generate-personas")
def create_personas(request: ResearchRequest):

    initial_state = {
        "product_name": request.product_name,
        "product_description": request.product_description,
        "target_audience": request.target_audience,
        "features": request.features,
        "research_objective": request.research_objective,
        "number_of_personas": request.number_of_personas,
        "personas": [],
        "survey_responses": [],
        "insights": ""
    }

    result = research_graph.invoke(initial_state)

    return {
        "product_name": result["product_name"],
        "target_audience": result["target_audience"],
        "personas": result["personas"],
        "survey_responses": result.get("survey_responses", []),
        "insights": result.get("insights", "")
    }


@app.post("/survey")
def run_survey(
    personas: list[Persona],
    question: str
):
    responses = conduct_survey(
        personas,
        question
    )

    return {
        "question": question,
        "responses": responses
    }


@app.post("/interview")
def run_interview(
    persona: Persona,
    question: str
):
    answer = conduct_interview(
        persona,
        question
    )

    return {
        "persona": persona.name,
        "question": question,
        "answer": answer
    }


@app.post("/insights")
def run_insights(
    product_name: str,
    research_objective: str,
    survey_responses: list
):
    insights = extract_insights(
        product_name,
        research_objective,
        survey_responses
    )

    return {
        "product_name": product_name,
        "insights": insights
    }


@app.post("/generate-report")
def create_report(request: ReportRequest):

    report_path = generate_report(
        product_name=request.product_name,
        research_objective=request.research_objective,
        personas=request.personas,
        survey_responses=request.survey_responses,
        insights=request.insights
    )

    return {
        "message": "Research report generated successfully",
        "report_path": report_path
    }