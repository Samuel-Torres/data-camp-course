import os
from pathlib import Path

import dotenv
from openai import OpenAI

dotenv.load_dotenv(Path(__file__).resolve().parent / ".env")

MEETING_PARAGRAPH = """
Quarterly planning sync, March 12. Attendees: Maya Chen (PM), Jordan Lee (Engineering),
and Priya Patel (Sales). Maya opened by noting Q1 revenue landed at 94% of target; Priya
attributed the shortfall to two delayed enterprise deals now expected to close in April.
Jordan reported that the new checkout flow reduced cart abandonment by 11% in the pilot
but uncovered a payment edge case affecting about 0.4% of transactions; a hotfix is
scheduled for release next Tuesday. The team agreed to pause the mobile redesign until
that fix ships, then resume with a two-week sprint focused on accessibility. Maya
assigned follow-ups: Priya to send revised forecasts by Friday, Jordan to post incident
notes in the shared doc, and everyone to review the updated roadmap draft before the
all-hands on the 20th.
""".strip()

summarization_prompt = (
    "Summarize the following business meeting notes in exactly 3 bullet points. "
    "Use a leading hyphen and space for each bullet (e.g. '- ...'). "
    "Be concise and capture the main outcomes and decisions.\n\n"
    f"{MEETING_PARAGRAPH}"
)


def run():
    """Run the main function."""
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        # Simple question based prompt:
        # messages=[{"role": "user", "content": "When was Donald Trump born?"}],
        # text editing prompt:
        # messages=[
        #     {
        #         "role": "user",
        #         "content": "Update Leah's last name to 'Torres' & just output the updated name in the following name: Leah Johnson.'",
        #     }
        # ],
        # Text summarization prompt:
        # messages=[{"role": "user", "content": summarization_prompt}],
        # max completion tokens (is a limit on the number of tokens that can be generated in the response. This is useful to control the cost of the request).
        # compare:
        # max_completion_tokens=50,
        # max_completion_tokens=100,
        # temperature: ranges from 0 to 2: 0 is highly deterministic while 2 is highly random. Default is 1.
        messages=[{"role": "user", "content": summarization_prompt}],
    )
    return response.choices[0].message.content or ""


if __name__ == "__main__":
    print(run())
