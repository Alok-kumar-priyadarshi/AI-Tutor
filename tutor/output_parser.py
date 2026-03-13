def parse_tutor_response(text):

    sections = {
        "concept": "",
        "analogy": "",
        "example": "",
        "question": ""
    }

    lines = text.split("\n")

    current_section = None

    for line in lines:

        lower = line.lower()

        if "concept explanation" in lower:
            current_section = "concept"
            continue

        if "real world analogy" in lower:
            current_section = "analogy"
            continue

        if "example" in lower:
            current_section = "example"
            continue

        if "practice question" in lower:
            current_section = "question"
            continue

        if current_section:
            sections[current_section] += line + "\n"

    return sections
