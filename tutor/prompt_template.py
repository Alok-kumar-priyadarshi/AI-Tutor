def build_tutor_prompt(topic, difficulty):

    prompt = f"""
You are an AI tutor.

Teach the topic clearly.

Topic: {topic}
Difficulty: {difficulty}

Return your answer ONLY in valid JSON.

Format:

{{
 "concept": "...",
 "analogy": "...",
 "example": "...",
 "practice_question": "..."
}}

Rules:
- Do not include extra text
- Do not explain outside JSON
"""

    return prompt