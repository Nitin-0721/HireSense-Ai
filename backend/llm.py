import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def ask_llm(context, question):

    prompt = f"""
You are an AI Resume Assistant.

Use ONLY the context below to answer.

Context:
{context}

Question:
{question}

If the answer is not present in the context, reply:
"I couldn't find that information in the resume."
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

    return response.choices[0].message.content