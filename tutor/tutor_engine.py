from groq import Groq
from config.settings import GROQ_API_KEY
from tutor.prompt_template import build_answer_evaluation_prompt

client = Groq(api_key=GROQ_API_KEY)

model_id = "openai/gpt-oss-120b"


def chat_with_tutor(messages):

    response = client.chat.completions.create(
        model=model_id,
        messages=messages
    )

    return response.choices[0].message.content

def evaluate_answer(question, student_answer):

    prompt = build_answer_evaluation_prompt(question, student_answer)

    response = client.chat.completions.create(
        model=model_id,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content