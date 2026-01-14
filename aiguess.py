import streamlit as st

st.title("🤖 AI Quiz Guessing Game")

questions = [
    {
        "question": "What does AI stand for?",
        "options": ["Artificial Intelligence", "Auto Input", "Advanced Internet"],
        "answer": "Artificial Intelligence"
    },
    {
        "question": "Which language is best for AI?",
        "options": ["Python", "C", "HTML"],
        "answer": "Python"
    }
]

# session state
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.finished = False

# quiz finished
if st.session_state.finished:
    st.success("🎉 Quiz Completed!")
    st.write(f"🏆 Your Score: {st.session_state.score}/{len(questions)}")
    
    # 🎈 BALLOONS HERE
    st.balloons()

    if st.button("Restart Quiz"):
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.session_state.finished = False

else:
    q = questions[st.session_state.q_index]
    st.subheader(q["question"])
    choice = st.radio("Choose one:", q["options"])

    if st.button("Submit"):
        if choice == q["answer"]:
            st.success("Correct ✅")
            st.session_state.score += 1
        else:
            st.error(f"Wrong ❌ Correct: {q['answer']}")

        if st.session_state.q_index < len(questions) - 1:
            st.session_state.q_index += 1
        else:
            st.session_state.finished = True
