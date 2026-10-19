from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
    product_name: str,
    research_objective: str,
    personas: list,
    survey_responses: list,
    insights: str
):
    output_path = "../reports/Smart_Student_Planner_Report.pdf"

    document = SimpleDocTemplate(
        output_path,
        pagesize=A4
    )

    styles = getSampleStyleSheet()
    story = []

    story.append(
        Paragraph(
            "Synthetic User Research Report",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            f"<b>Product:</b> {product_name}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1, 10))

    story.append(
        Paragraph(
            f"<b>Research Objective:</b> {research_objective}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "Synthetic Personas",
            styles["Heading2"]
        )
    )

    for persona in personas:
        story.append(
            Paragraph(
                f"<b>{persona.name}</b> — "
                f"{persona.age} years old, "
                f"{persona.occupation}",
                styles["Normal"]
            )
        )

        story.append(
            Paragraph(
                f"Goals: {', '.join(persona.goals)}",
                styles["Normal"]
            )
        )

        story.append(
            Paragraph(
                f"Pain Points: {', '.join(persona.pain_points)}",
                styles["Normal"]
            )
        )

        story.append(Spacer(1, 10))

    story.append(
        Paragraph(
            "Survey Responses",
            styles["Heading2"]
        )
    )

    for response in survey_responses:
        story.append(
            Paragraph(
                f"<b>{response['persona']}</b>: "
                f"{response['answer']}",
                styles["Normal"]
            )
        )

        story.append(Spacer(1, 8))

    story.append(
        Paragraph(
            "Research Insights",
            styles["Heading2"]
        )
    )

    for line in insights.split("\n"):
        if line.strip():
            story.append(
                Paragraph(
                    line,
                    styles["Normal"]
                )
            )

            story.append(Spacer(1, 5))

    story.append(Spacer(1, 15))

    story.append(
        Paragraph(
            "<b>Important:</b> These findings are generated "
            "from fictional AI-powered synthetic users and "
            "should not be treated as real-world user research.",
            styles["Normal"]
        )
    )

    document.build(story)

    return output_path