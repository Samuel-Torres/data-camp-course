import os
from pathlib import Path

import dotenv
from openai import OpenAI

dotenv.load_dotenv(Path(__file__).resolve().parent / ".env")


def run():
    """Run the main function."""
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "When was Donald Trump born?"}],
    )
    return response.choices[0].message.content or ""


if __name__ == "__main__":
    print(run())
