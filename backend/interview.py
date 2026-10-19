from agent import llm
from memory import persona_memory
from models import Persona
from database import save_interview_response


def conduct_interview(
    persona: Persona,
    question: str
):
    persona_id = persona.name

    # Get previous memory
    memory = persona_memory.get_memory(persona_id)

    conversation = memory["conversation"]
    opinions = memory["opinions"]

    prompt = f"""
You are participating in a synthetic user research interview.

You are NOT a real person.
You are a fictional synthetic persona.

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

PREVIOUS OPINIONS:
{opinions}

PREVIOUS CONVERSATION:
{conversation}

INTERVIEW QUESTION:
{question}

Instructions:
1. Answer naturally as this fictional persona.
2. Stay consistent with the persona's characteristics.
3. Use previous conversation and opinions when relevant.
4. Do not suddenly change your preferences without a reasonable explanation.
5. Give a realistic student-style response.
6. Do not mention that you are an AI unless necessary.
"""

    # Ask Gemini to generate the persona's answer
    response = llm.invoke(prompt)

    answer = response.content

    # Handle Gemini structured content if returned as a list
    if isinstance(answer, list):
        answer = "".join(
            item.get("text", "")
            for item in answer
            if isinstance(item, dict)
        )

    # Save this interaction to memory
    persona_memory.add_conversation(
        persona_id,
        question,
        answer
    )

    # Save important opinion related to the question
    persona_memory.add_opinion(
        persona_id,
        question,
        answer
    )

    # Save interview response to SQLite database
    save_interview_response(
        persona.name,
        question,
        answer
    )

    return answer