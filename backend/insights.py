from agent import llm


def extract_insights(
    product_name: str,
    research_objective: str,
    survey_responses: list
):
    formatted_responses = ""

    for response in survey_responses:
        formatted_responses += (
            f"\nPersona: {response['persona']}\n"
            f"Response: {response['answer']}\n"
        )

    prompt = f"""
You are an AI-powered Product Research Insight Extraction Agent.

PRODUCT:
{product_name}

RESEARCH OBJECTIVE:
{research_objective}

SYNTHETIC SURVEY RESPONSES:
{formatted_responses}

Analyze the responses and produce a structured research summary.

Include the following sections:

1. Key Insights
2. Common Pain Points
3. Most Useful Features
4. Pricing and Willingness to Pay
5. Differences Between Personas
6. Product Recommendations
7. Overall Summary

IMPORTANT:
- These are AI-generated synthetic users.
- Do not claim that the findings represent real students.
- Clearly distinguish simulated insights from real-world research.
- Base the analysis only on the provided responses.
- Do not invent statistics or responses.
"""

    response = llm.invoke(prompt)

    insights = response.content

    if isinstance(insights, list):
        insights = "".join(
            item.get("text", "")
            for item in insights
            if isinstance(item, dict)
        )

    return insights