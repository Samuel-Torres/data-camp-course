"""

Step-by-step prompting.
"""

import os
from pathlib import Path

import dotenv
from openai import OpenAI

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
dotenv.load_dotenv(_PROJECT_ROOT / ".env")

MULTIPLE_STEP_PROMPT = """
    Compose a travel blog post as follows:
    Step 1: Introduce the destination.
    Step 2: Share personal adventures during the trip.
    Step 3: Summarize the journey.
"""


def run() -> str:
    """
    shot prompting with a single user message.
    """
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": MULTIPLE_STEP_PROMPT}],
    )
    return response.choices[0].message.content or ""


if __name__ == "__main__":
    print(run())
