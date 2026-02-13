import streamlit as st

st.title("🌟 Kids Bible Quiz App 🌟")
st.write("Choose the correct answer and click **Next Question**.")

quiz = [
    {
        "question": "What is the first book of the Old Testament?",
        "options": ["Genesis", "Exodus", "Leviticus", "Numbers"],
        "answer": "Genesis"
    },
    {
        "question": "Who built the ark to survive the flood?",
        "options": ["Moses", "Noah", "Abraham", "David"],
        "answer": "Noah"
    },
    {
        "question": "Who was thrown into the lion's den?",
        "options": ["Daniel", "Jonah", "Joseph", "Samuel"],
        "answer": "Daniel"
    },
    {
        "question": "Who led the Israelites out of Egypt?",
        "options": ["Joshua", "Moses", "Aaron", "Caleb"],
        "answer": "Moses"
    },
    {
        "question": "What did David use to defeat Goliath?",
        "options": ["Sword", "Sling and stone", "Spear", "Bow and arrow"],
        "answer": "Sling and stone"
    },
    {
        "question": "Who was swallowed by a big fish?",
        "options": ["Peter", "Jonah", "Elijah", "Paul"],
        "answer": "Jonah"
    },
    {
        "question": "How many days and nights did it rain during the flood?",
        "options": ["20", "30", "40", "50"],
        "answer": "40"
    },
    {
        "question": "Who was the mother of Jesus?",
        "options": ["Elizabeth", "Mary", "Martha", "Ruth"],
        "answer": "Mary"
    },
    {
        "question": "What is the shortest verse in the Bible?",
        "options": ["Jesus wept", "Pray without ceasing", "God is love", "Love your neighbor"],
        "answer": "Jesus wept"
    },
    {
        "question": "Who interpreted Pharaoh’s dreams?",
        "options": ["Moses", "Joseph", "Daniel", "Samuel"],
        "answer": "Joseph"
    },
    {
        "question": "What did Jesus feed 5000 people with?",
        "options": ["Bread and fish", "Water and wine", "Manna", "Olives"],
        "answer": "Bread and fish"
    },
    {
        "question": "Who betrayed Jesus for 30 pieces of silver?",
        "options": ["Peter", "Judas", "John", "Thomas"],
        "answer": "Judas"
    }
]

# Initialize session state
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
    st.session_state.score = 0

q = quiz[st.session_state.question_index]

st.subheader(f"Question {st.session_state.question_index + 1}")
st.write(q["question"])

choice = st.radio("Choose an answer:", q["options"])

if st.button("Next Question"):
    if choice == q["answer"]:
        st.success("Correct!")
        st.session_state.score += 1
    else:
        st.error(f"Wrong! Correct answer is: {q['answer']}")

    st.session_state.question_index += 1

    if st.session_state.question_index >= len(quiz):
        st.balloons()
        st.write(f"🎉 Quiz Finished! Your score: {st.session_state.score} / {len(quiz)}")
        st.stop()

    st.experimental_rerun()