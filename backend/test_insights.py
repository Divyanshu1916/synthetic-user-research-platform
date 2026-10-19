from insights import extract_insights


survey_responses = [
    {
        "persona": "Aarav Sharma",
        "answer": (
            "I would pay ₹99 per month if the AI timetable and "
            "progress tracking genuinely improve my productivity and grades."
        )
    },
    {
        "persona": "Ananya Patel",
        "answer": (
            "I would not pay ₹99 per month because I have a limited budget. "
            "I would prefer a free plan with assignment reminders and exam countdown."
        )
    },
    {
        "persona": "Rohan Verma",
        "answer": (
            "I would pay ₹99 per month because the AI timetable and progress "
            "tracking would help me manage procrastination and study time."
        )
    }
]


insights = extract_insights(
    product_name="Smart Student Planner",
    research_objective=(
        "Understand student preferences, pain points, "
        "feature usefulness, and willingness to pay."
    ),
    survey_responses=survey_responses
)


print("\n========== RESEARCH INSIGHTS ==========\n")
print(insights)