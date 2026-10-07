
import streamlit as st
import random

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="IPL Quiz Challenge",
    page_icon="🏏",
    layout="centered"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #070b18, #101936, #070b18);
    color: white;
}

.main-title {
    text-align: center;
    font-size: 45px;
    font-weight: 800;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #b8c2d9;
    margin-bottom: 30px;
}

.quiz-card {
    background: rgba(255,255,255,0.07);
    padding: 25px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.12);
    margin-bottom: 20px;
}

.trophy {
    text-align: center;
    font-size: 100px;
}

.winner {
    text-align: center;
    font-size: 32px;
    font-weight: 800;
}

.score {
    text-align: center;
    font-size: 25px;
    margin-top: 10px;
}

.small-text {
    text-align: center;
    color: #aeb8cf;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# QUIZ QUESTIONS
# =========================================================

questions = [
    {
        "question": "Who won the first IPL season in 2008?",
        "options": [
            "Chennai Super Kings",
            "Rajasthan Royals",
            "Mumbai Indians",
            "Kolkata Knight Riders"
        ],
        "answer": "Rajasthan Royals"
    },

    {
        "question": "Which team has traditionally been known as the 'Men in Yellow'?",
        "options": [
            "Mumbai Indians",
            "Royal Challengers Bengaluru",
            "Chennai Super Kings",
            "Delhi Capitals"
        ],
        "answer": "Chennai Super Kings"
    },

    {
        "question": "Who is popularly known as the 'King of IPL'?",
        "options": [
            "Virat Kohli",
            "Rohit Sharma",
            "MS Dhoni",
            "AB de Villiers"
        ],
        "answer": "Virat Kohli"
    },

    {
        "question": "Which IPL team is based in Kolkata?",
        "options": [
            "Kolkata Knight Riders",
            "Punjab Kings",
            "Delhi Capitals",
            "Sunrisers Hyderabad"
        ],
        "answer": "Kolkata Knight Riders"
    },

    {
        "question": "What does IPL stand for?",
        "options": [
            "Indian Players League",
            "Indian Premier League",
            "International Premier League",
            "India Professional League"
        ],
        "answer": "Indian Premier League"
    },

    {
        "question": "Which player is famously known as 'Captain Cool'?",
        "options": [
            "Virat Kohli",
            "Hardik Pandya",
            "MS Dhoni",
            "Rohit Sharma"
        ],
        "answer": "MS Dhoni"
    }
]


# =========================================================
# SESSION STATE
# =========================================================

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "selected_answers" not in st.session_state:
    st.session_state.selected_answers = {}

if "quiz_finished" not in st.session_state:
    st.session_state.quiz_finished = False


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🏏 IPL QUIZ CHALLENGE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Test your IPL knowledge and win the Trophy! 🏆</div>',
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# START SCREEN
# =========================================================

if not st.session_state.quiz_started:

    st.markdown(
        """
        <div class="quiz-card">
        <h2 style="text-align:center;">🔥 Are You a True IPL Fan?</h2>
        <p style="text-align:center;color:#b8c2d9;">
        Answer 6 IPL questions and prove your cricket knowledge.
        </p>
        <p style="text-align:center;">
        🏏 6 Questions &nbsp; | &nbsp;
        🎯 4+ Correct = Trophy &nbsp; | &nbsp;
        ❌ Below 4 = No Trophy
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "🚀 START IPL QUIZ",
        use_container_width=True
    ):
        st.session_state.quiz_started = True
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.selected_answers = {}
        st.session_state.quiz_finished = False
        st.rerun()


# =========================================================
# QUIZ SCREEN
# =========================================================

elif not st.session_state.quiz_finished:

    question_number = st.session_state.current_question

    total_questions = len(questions)

    question = questions[question_number]

    # Progress
    progress = (question_number) / total_questions

    st.progress(progress)

    st.caption(
        f"Question {question_number + 1} of {total_questions}"
    )

    st.markdown(
        f"""
        <div class="quiz-card">
        <h2>🏏 {question["question"]}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    answer = st.radio(
        "Select your answer:",
        question["options"],
        key=f"question_{question_number}"
    )

    st.write("")

    if st.button(
        "NEXT QUESTION ➜",
        use_container_width=True
    ):

        # Check answer
        if answer == question["answer"]:
            st.session_state.score += 1

        # Move to next question
        if question_number + 1 < total_questions:

            st.session_state.current_question += 1
            st.rerun()

        else:

            st.session_state.quiz_finished = True
            st.rerun()


# =========================================================
# RESULT SCREEN
# =========================================================

else:

    score = st.session_state.score
    total = len(questions)

    st.divider()

    if score >= 4:

        # =========================
        # WINNER
        # =========================

        st.markdown(
            '<div class="trophy">🏆</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="winner">CONGRATULATIONS!</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="score">You Won the IPL Trophy! 🏆</div>',
            unsafe_allow_html=True
        )

        st.success(
            f"🎉 You scored {score}/{total}. "
            "You are a true IPL champion!"
        )

        st.balloons()

    else:

        # =========================
        # LOSER
        # =========================

        st.markdown(
            '<div class="trophy">🏏</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="winner">BETTER LUCK NEXT TIME!</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="score">No Trophy This Time ❌</div>',
            unsafe_allow_html=True
        )

        st.error(
            f"You scored {score}/{total}. "
            "You need at least 4 correct answers to win the Trophy."
        )

    st.divider()

    # Score summary
    percentage = int((score / total) * 100)

    st.metric(
        label="Your Final Score",
        value=f"{score} / {total}"
    )

    st.progress(score / total)

    st.caption(
        f"Accuracy: {percentage}%"
    )

    st.write("")

    # Restart
    if st.button(
        "🔄 PLAY AGAIN",
        use_container_width=True
    ):

        st.session_state.quiz_started = False
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.selected_answers = {}
        st.session_state.quiz_finished = False

        st.rerun()


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <p style="text-align:center;color:#7f8aa3;">
    🏏 IPL Quiz Challenge • Built with Streamlit
    </p>
    """,
    unsafe_allow_html=True
)