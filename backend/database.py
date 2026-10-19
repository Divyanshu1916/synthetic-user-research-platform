import sqlite3


DATABASE_NAME = "../data/research.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS personas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            education TEXT,
            occupation TEXT,
            personality_traits TEXT,
            behavioral_patterns TEXT,
            psychological_profile TEXT,
            goals TEXT,
            pain_points TEXT,
            preferred_features TEXT,
            price_sensitivity TEXT,
            willingness_to_pay TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS survey_responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            persona_name TEXT NOT NULL,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS interviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            persona_name TEXT NOT NULL,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_persona(persona):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO personas (
            name,
            age,
            education,
            occupation,
            personality_traits,
            behavioral_patterns,
            psychological_profile,
            goals,
            pain_points,
            preferred_features,
            price_sensitivity,
            willingness_to_pay
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        persona.name,
        persona.age,
        persona.education,
        persona.occupation,
        ", ".join(persona.personality_traits),
        ", ".join(persona.behavioral_patterns),
        ", ".join(persona.psychological_profile),
        ", ".join(persona.goals),
        ", ".join(persona.pain_points),
        ", ".join(persona.preferred_features),
        persona.price_sensitivity,
        persona.willingness_to_pay
    ))

    connection.commit()
    connection.close()


def save_survey_response(
    persona_name: str,
    question: str,
    answer: str
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO survey_responses (
            persona_name,
            question,
            answer
        )
        VALUES (?, ?, ?)
    """, (
        persona_name,
        question,
        answer
    ))

    connection.commit()
    connection.close()


# ADD THIS FUNCTION HERE
def save_interview_response(
    persona_name: str,
    question: str,
    answer: str
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO interviews (
            persona_name,
            question,
            answer
        )
        VALUES (?, ?, ?)
    """, (
        persona_name,
        question,
        answer
    ))

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_tables()
    print("Database tables created successfully.")