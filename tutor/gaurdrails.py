blocked_topics = [
    "bomb",
    "weapon",
    "kill",
    "hack",
    "illegal",
    "drugs"
]


def is_topic_safe(topic):

    topic_lower = topic.lower()

    for word in blocked_topics:
        if word in topic_lower:
            return False

    return True