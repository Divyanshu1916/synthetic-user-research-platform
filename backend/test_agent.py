from agent import generate_personas
from models import ResearchRequest


request = ResearchRequest(
    product_name="Smart Student Planner",
    product_description=(
        "An AI-powered study planner with timetable creation, "
        "assignment reminders, exam countdown, and progress tracking. "
        "Premium plan costs ₹99 per month."
    ),
    target_audience="School and college students",
    features=[
        "AI-powered study timetable",
        "Assignment reminders",
        "Exam countdown",
        "Progress tracking",
        "₹99/month premium plan"
    ],
    research_objective=(
        "Understand student preferences, pain points, "
        "feature usefulness, and willingness to pay."
    ),
    number_of_personas=3
)


result = generate_personas(request)

for i, persona in enumerate(result.personas, start=1):
    print(f"\n--- Persona {i} ---")
    print(f"Name: {persona.name}")
    print(f"Age: {persona.age}")
    print(f"Education: {persona.education}")
    print(f"Occupation: {persona.occupation}")
    print(f"Personality: {persona.personality_traits}")
    print(f"Behavior: {persona.behavioral_patterns}")
    print(f"Psychological Profile: {persona.psychological_profile}")
    print(f"Goals: {persona.goals}")
    print(f"Pain Points: {persona.pain_points}")
    print(f"Preferred Features: {persona.preferred_features}")
    print(f"Price Sensitivity: {persona.price_sensitivity}")
    print(f"Willingness to Pay: {persona.willingness_to_pay}")