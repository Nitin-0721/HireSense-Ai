import json
from llm import client


def analyze_resume(resume_text, jd_text):
    prompt = f"""
You are an expert ATS (Applicant Tracking System).

Compare the following Resume and Job Description.

Return ONLY valid JSON in this format:

{{
    "ats_score": 85,
    "matching_skills": [
        "...",
        "..."
    ],
    "missing_skills": [
        "...",
        "..."
    ],
    "summary": "...",
    "suggestions": [
        "...",
        "..."
    ],
    "interview_questions": [
        "...",
        "...",
        "...",
        "...",
        "..."
    ]
}}

Resume:
{resume_text}

Job Description:
{jd_text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    result = response.choices[0].message.content

    result = result.replace("```json", "").replace("```", "").strip()

    return json.loads(result)