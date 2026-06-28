import streamlit as st
import requests
import json

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="HireSense AI",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Session State
# -----------------------------
if "resume_uploaded" not in st.session_state:
    st.session_state.resume_uploaded = False

if "analysis" not in st.session_state:
    st.session_state.analysis = None

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>

.main{
    background:#f8fafc;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

.title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#2563eb;
}

.subtitle{
    text-align:center;
    color:gray;
    font-size:18px;
    margin-bottom:30px;
}

.card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0 0 10px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown(
    "<div class='title'>🤖 HireSense AI</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>AI Resume Intelligence Platform</div>",
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# Upload Section
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Resume")
    resume = st.file_uploader(
        "Upload Resume",
        type=["pdf"],
        key="resume"
    )

with col2:
    st.subheader("📋 Job Description")
    jd = st.file_uploader(
        "Upload JD",
        type=["pdf"],
        key="jd"
    )

st.divider()

# -----------------------------
# Analyze Button
# -----------------------------
if st.button("🚀 Analyze Resume", use_container_width=True):

    if resume is None:
        st.warning("Please upload your resume.")
        st.stop()

    files = {
        "file": (
            resume.name,
            resume.getvalue(),
            "application/pdf"
        )
    }

    with st.spinner("Uploading Resume..."):
        response = requests.post(
            f"{API_URL}/upload-resume",
            files=files
        )

    if response.status_code != 200:
        st.error("Resume upload failed.")
        st.stop()

    st.session_state.resume_uploaded = True
    st.success("Resume uploaded successfully.")

    if jd is not None:
        jd_files = {
            "file": (
                jd.name,
                jd.getvalue(),
                "application/pdf"
            )
        }

        with st.spinner("Analyzing Resume..."):
            ats = requests.post(
                f"{API_URL}/ats",
                files=jd_files
            )

        if ats.status_code == 200:
            st.session_state.analysis = ats.json()
        else:
            st.error("ATS Analysis Failed.")

st.divider()

# -----------------------------
# ATS Results
# -----------------------------
analysis = st.session_state.analysis

if analysis is not None:
    st.subheader("📊 ATS Analysis")

    score = analysis.get("ats_score", 0)
    st.progress(score / 100)
    st.metric("ATS Score", f"{score}%")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Matching Skills")
        for skill in analysis.get("matching_skills", []):
            st.success(skill)

    with col2:
        st.subheader("❌ Missing Skills")
        for skill in analysis.get("missing_skills", []):
            st.error(skill)

    st.divider()

    st.subheader("📝 Resume Summary")
    st.info(analysis.get("summary", ""))

    st.divider()

    st.subheader("💡 AI Suggestions")
    suggestions = analysis.get("suggestions", [])
    for suggestion in suggestions:
        st.write("•", suggestion)

    st.divider()

    st.subheader("🎯 Interview Questions")
    questions = analysis.get("interview_questions", [])
    for i, q in enumerate(questions, 1):
        st.write(f"{i}. {q}")

st.divider()

# -----------------------------
# Chat Section
# -----------------------------
st.subheader("💬 Chat with Resume")

question = st.text_input(
    "Ask anything about your resume",
    placeholder="Example: Summarize my projects"
)

if st.button("Ask AI"):

    if question.strip() == "":
        st.warning("Please enter a question.")
        st.stop()

    response = requests.post(
        f"{API_URL}/chat",
        json={
            "question": question
        }
    )

    if response.status_code == 200:
        answer = response.json()["answer"]
        st.session_state.messages.append(
            {
                "question": question,
                "answer": answer
            }
        )
    else:
        st.error("Chat failed.")

if st.session_state.messages:
    st.divider()
    for msg in reversed(st.session_state.messages):
        with st.chat_message("user"):
            st.write(msg["question"])
        with st.chat_message("assistant"):
            st.write(msg["answer"])