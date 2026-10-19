from models import Persona
from interview import conduct_interview


persona = Persona(
    name="Ananya Patel",
    age=16,
    education="High School Student",
    occupation="Student",
    personality_traits=[
        "Budget-conscious",
        "Organized",
        "Practical"
    ],
    behavioral_patterns=[
        "Uses free study tools",
        "Plans around exams",
        "Avoids recurring expenses"
    ],
    psychological_profile=[
        "Values academic improvement",
        "Sensitive to pricing",
        "Prefers simple solutions"
    ],
    goals=[
        "Improve grades",
        "Complete assignments on time"
    ],
    pain_points=[
        "Heavy school workload",
        "Difficulty maintaining a consistent schedule"
    ],
    preferred_features=[
        "Assignment reminders",
        "Exam countdown"
    ],
    price_sensitivity="High",
    willingness_to_pay="Low"
)


question = "Would you pay ₹99 per month for this Smart Student Planner? Why?"

answer = conduct_interview(
    persona,
    question
)

print("\nPersona:", persona.name)
print("Question:", question)
print("Answer:", answer)