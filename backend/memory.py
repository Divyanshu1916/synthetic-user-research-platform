class PersonaMemory:
    def __init__(self):
        self.memory = {}

    def create_persona(self, persona_id: str):
        self.memory[persona_id] = {
            "conversation": [],
            "opinions": {}
        }

    def add_conversation(
        self,
        persona_id: str,
        question: str,
        answer: str
    ):
        if persona_id not in self.memory:
            self.create_persona(persona_id)

        self.memory[persona_id]["conversation"].append({
            "question": question,
            "answer": answer
        })

    def add_opinion(
        self,
        persona_id: str,
        topic: str,
        opinion: str
    ):
        if persona_id not in self.memory:
            self.create_persona(persona_id)

        self.memory[persona_id]["opinions"][topic] = opinion

    def get_memory(self, persona_id: str):
        return self.memory.get(
            persona_id,
            {
                "conversation": [],
                "opinions": {}
            }
        )


persona_memory = PersonaMemory()