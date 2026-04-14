"""
chat roles, system messages.
"""

from __future__ import annotations

import os
from pathlib import Path

import dotenv
from openai import OpenAI

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
dotenv.load_dotenv(_PROJECT_ROOT / ".env")

sys_msg = """
You are finance education assistant that helps students study for exams.
If you are asked for specific, real-world financial advice with risk to their finances, respond with:
I'm sorry, I am not allowed to provide financial advice.
"""


# def run() -> str:
#     """
#     shot prompting with a single user message.
#     """
#     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a Python programming tutor who speaks concisely.",
#             },
#             {
#                 "role": "user",
#                 "content": "What is the difference between mutable and immutable objects?",
#             },
#         ],
#     )
#     return response.choices[0].message.content or ""


# example of a system message with gaurdrails:
# def run() -> str:
#     """example of a system message"""
#     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": sys_msg},
#             {
#                 "role": "user",
#                 "content": "I have a roth IRA where should I invest my money?",
#             },
#         ],
#     )
#     return response.choices[0].message.content or ""


# assistant role:
# you can add an example of the assistant ideal response after the system message as an example of a user message followed up with a assistant response.
# def run() -> str:
#     """
#     assistant role:
#     """
#     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a Python programming tutor who speaks concisely. You are also a complete and utter asshole who swears a lot.",
#             },
#             {"role": "user", "content": "How do you define a Python list?"},
#             {
#                 "role": "assistant",
#                 "content": "Alright asshole, let me exaplain like you're a 5 year old. Lists are defined by enclosing a comma-separated sequence of objects inside square brackets [ ].",
#             },
#             {
#                 "role": "user",
#                 "content": "What is the difference between mutable and immutable objects?",
#             },
#         ],
#     )
#     return response.choices[0].message.content or ""


# multiple turn conversations:
def run() -> str:
    """
    assistant role:
    """
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    messages = [
        {
            "role": "system",
            "content": "You are a data science tutor who provides short, simple explanations.",
        },
    ]
    user_qs = ["Why is Python so popular?", "Summarize this in one sentence."]
    for user_q in user_qs:
        print(f"User question: {user_q}")
        user_dict = {"role": "user", "content": user_q}
        messages.append(user_dict)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
        )

        assistant_dict = {
            "role": "assistant",
            "content": response.choices[0].message.content,
        }
        messages.append(assistant_dict)
        print(f"Assistant response: {response.choices[0].message.content}")


if __name__ == "__main__":
    print(run())
