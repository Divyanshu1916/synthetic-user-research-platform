from models import Persona
from survey import conduct_survey


personas = [
    Persona(
        name="Aarav Sharma",
        age=20,
        education="B.Tech Computer Science",
        occupation="Engineering Student",
        personality_traits=[
            "Analytical",
            "Goal-oriented",
            "Tech-savvy"
        ],
        behavioral_patterns=[
            "Plans study sessions",
            "Uses productivity apps regularly"
        ],
        psychological_profile=[
            "Values efficiency",
            "Wants better academic performance"
        ],
        goals=[
            "Improve grades",
            "Manage study time efficiently"
        ],
        pain_points=[
            "Difficulty balancing multiple subjects",
            "Inconsistent study schedule"
        ],
        preferred_features=[
            "AI-powered study timetable",
            "Progress tracking"
        ],
        price_sensitivity="Low",
        willingness_to_pay="High"
    ),

    Persona(
        name="Ananya Patel",
        age=16,
        education="Class 11",
        occupation="High School Student",
        personality_traits=[
            "Disciplined",
            "Budget-conscious",
            "Goal-oriented"
        ],
        behavioral_patterns=[
            "Studies mainly before exams",
            "Uses reminders for assignments"
        ],
        psychological_profile=[
            "Wants academic stability",
            "Avoids unnecessary expenses"
        ],
        goals=[
            "Improve exam preparation",
            "Complete assignments on time"
        ],
        pain_points=[
            "Forgets assignments",
            "Limited budget for paid apps"
        ],
        preferred_features=[
            "Exam countdown",
            "Assignment reminders"
        ],
        price_sensitivity="High",
        willingness_to_pay="Low"
    ),

    Persona(
        name="Rohan Verma",
        age=21,
        education="B.A. English Literature",
        occupation="College Student",
        personality_traits=[
            "Creative",
            "Procrastinator",
            "Adaptable",
            "Social"
        ],
        behavioral_patterns=[
            "Often delays tasks",
            "Uses digital tools when convenient"
        ],
        psychological_profile=[
            "Needs motivation",
            "Values simplicity"
        ],
        goals=[
            "Complete assignments on time",
            "Stay motivated"
        ],
        pain_points=[
            "Procrastination",
            "Difficulty estimating task duration"
        ],
        preferred_features=[
            "Progress tracking",
            "AI-powered study timetable",
            "Exam countdown"
        ],
        price_sensitivity="Moderate",
        willingness_to_pay="Moderate"
    )
]


question = "Would you pay ₹99 per month for the Smart Student Planner?"

responses = conduct_survey(
    personas,
    question
)


print("\n--- Survey Results ---")

for response in responses:
    print(f"\nPersona: {response['persona']}")
    print(f"Answer: {response['answer']}")