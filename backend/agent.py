from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from models import ResearchRequest, PersonaList
from prompts import PERSONA_GENERATION_PROMPT

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

persona_llm = llm.with_structured_output(PersonaList)


def generate_personas(request: ResearchRequest) -> PersonaList:
    prompt = PERSONA_GENERATION_PROMPT.format(
        product_name=request.product_name,
        product_description=request.product_description,
        target_audience=request.target_audience,
        features=", ".join(request.features),
        research_objective=request.research_objective,
        number_of_personas=request.number_of_personas
    )

    response = persona_llm.invoke(prompt)

    return response