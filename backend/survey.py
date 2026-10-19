from typing import List

from agent import llm
from database import save_survey_response

from models import Persona

def conduct_survey(
    personas: List[Persona],
    question: str
):
    responses = []

    for persona in personas:

        prompt = f"""
You are a fictional synthetic user participating in a product research survey.

PERSONA:
Name: {persona.name}
Age: {persona.age}
Education: {persona.education}
Occupation: {persona.occupation}

Personality:
{persona.personality_traits}

Behavioral Patterns:
{persona.behavioral_patterns}

Psychological Profile:
{persona.psychological_profile}

Goals:
{persona.goals}

Pain Points:
{persona.pain_points}

Preferred Features:
{persona.preferred_features}

Price Sensitivity:
{persona.price_sensitivity}

Willingness to Pay:
{persona.willingness_to_pay}

SURVEY QUESTION:
{question}

Instructions:
1. Answer as this fictional persona.
2. Keep the answer consistent with the persona.
3. Consider the persona's goals, pain points, and preferences.
4. Give a natural and concise survey response.
5. Do not invent unrelated information.
"""

        # Ask Gemini to generate the persona's answer
        response = llm.invoke(prompt)

        # Extract only the text from Gemini's response
        answer = response.content

        if isinstance(answer, list):
            answer = "".join(
                item.get("text", "")
                for item in answer
                if isinstance(item, dict)
            )

        # Store the survey response
        responses.append({
            "persona": persona.name,
            "answer": answer
        })
        
        save_survey_response(
        persona.name,
        question,
        answer
        )

    return responses