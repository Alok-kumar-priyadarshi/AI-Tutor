from tutor.tutor_engine import chat_with_tutor, evaluate_answer
from tutor.prompt_template import create_system_prompt
import streamlit as st
from tutor.output_parser import parse_tutor_response
from tutor.gaurdrails import is_topic_safe



st.title("AI Toutor")
st.write("Learn any topic from AI tutor")

# initialize memory
if "messages" not in st.session_state:
    st.session_state.messages = []
    

if "practice_question" not in st.session_state:
    st.session_state.practice_question = ""
    
    

# user input
topic = st.text_input("Enter a topic")

difficulty = st.selectbox(
    "Select difficulty level",
    ["Beginner" , "Intermediate" , "Advanced"]
)

# generate button
if st.button("Start Lesson"):

    if topic.strip() == "":
        st.error("Please enter a topic first.")

    elif not is_topic_safe(topic):
        st.error("This topic is not allowed in the AI Tutor.")

    else:

        system_prompt = create_system_prompt(topic, difficulty)

        st.session_state.messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Teach me about {topic}"}
        ]

        response = chat_with_tutor(st.session_state.messages)

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )

        st.session_state.lesson_started = True

        st.rerun()
        
        
# display conversation

for msg in st.session_state.messages:
    if msg["role"] == "assistant":
        parsed = parse_tutor_response(msg["content"])

        with st.chat_message("assistant"):

            if parsed["concept"]:
                st.subheader("📘 Concept Explanation")
                st.write(parsed["concept"])

            if parsed["analogy"]:
                st.subheader("🧠 Real World Analogy")
                st.write(parsed["analogy"])

            if parsed["example"]:
                st.subheader("🔎 Example")
                st.write(parsed["example"])

            if parsed["question"]:
                st.subheader("✏ Practice Question")
                st.write(parsed["question"])

                # store question for evaluation
                st.session_state.practice_question = parsed["question"]
                
    if msg["role"] == "user":

        with st.chat_message("user"):
            st.write(msg["content"])
        



# follow-up chat input always visible

user_question = st.chat_input("Ask the AI Tutor")

if user_question:

    if topic.strip() == "":
        st.error("Please enter a topic first.")

    elif not is_topic_safe(topic):
        st.error("This topic is not allowed in the AI Tutor.")

    else:

        st.session_state.messages.append(
            {"role": "user", "content": user_question}
        )

        with st.chat_message("user"):
            st.write(user_question)

        response = chat_with_tutor(st.session_state.messages)

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )

        st.rerun()



# Answer Evaluation 


if st.session_state.practice_question:

    st.subheader("Submit Your Answer")

    student_answer = st.text_area("Your Answer")

    if st.button("Evaluate My Answer"):

        if student_answer.strip() == "":
            st.error("Please enter your answer.")

        else:

            evaluation = evaluate_answer(
                st.session_state.practice_question,
                student_answer
            )

            st.subheader("Tutor Feedback")

            st.write(evaluation)