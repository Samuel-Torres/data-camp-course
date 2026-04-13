"""
zero through multiple shot prompting.
"""

from __future__ import annotations

import os
from pathlib import Path

import dotenv
from openai import OpenAI

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
dotenv.load_dotenv(_PROJECT_ROOT / ".env")

ZERO_SHOT_PROMPT = """Classify sentiment as 1-5 (bad-good) in the following statements:
1. Meal was decent, but I've had better.
2. My food was delayed, but drinks were good.
"""

ONE_SHOT_PROMPT = """Classify sentiment as 1-5 (bad-good) in the following statements:
1. The service was very slow -> 1
2. Meal was decent, but I've had better. ->
3. My food was delayed, but drinks were good. -›
"""

MULTIPLE_SHOT_PROMPT = """Classify sentiment as 1-5 (bad-good) in the following statements:
1. The service was very slow -> 1

2. The steak was awfully good! -> 5

3. It was ok, no massive complaints. -> 3

4. Meal was decent, but I've had better. ->

5. My food was delayed, but drinks were good. -›
"""


def run() -> str:
    """
    shot prompting with a single user message.
    """
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        # messages=[{"role": "user", "content": ZERO_SHOT_PROMPT}],
        # messages=[{"role": "user", "content": ONE_SHOT_PROMPT}],
        messages=[{"role": "user", "content": MULTIPLE_SHOT_PROMPT}],
    )
    return response.choices[0].message.content or ""


if __name__ == "__main__":
    print(run())
