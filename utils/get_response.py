import os
from pathlib import Path

import dotenv
from openai import OpenAI

dotenv.load_dotenv(Path(__file__).resolve().parent / ".env")


def get_response(prompt: str) -> str:
    """Get a response from the OpenAI API."""
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )
    return response.choices[0].message.content or ""
