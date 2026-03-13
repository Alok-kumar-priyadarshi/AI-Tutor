import json


def parse_tutor_response(text):

    try:
        data = json.loads(text)
        return data

    except Exception:
        return {
            "concept": text,
            "analogy": "",
            "example": "",
            "practice_question": ""
        }