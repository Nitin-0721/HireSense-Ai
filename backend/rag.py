from utils import retrieve
from llm import ask_llm


def chat_with_resume(question):

    context = retrieve(question)

    answer = ask_llm(context, question)

    return answer