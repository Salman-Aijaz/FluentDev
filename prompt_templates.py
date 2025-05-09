meeting_script_prompt = """
You're simulating a 30-minute meeting between a 👤 Client and a 👨‍💻 Developer.

📝 Topic: {topic}

🎯 Goal: Generate a realistic back-and-forth conversation that spans approximately a 30-minute meeting. Include multiple follow-up questions, clarifications, and answers.

{technical_note}
{challenging_note}
{detailed_note}
{budget_note}

✅ Output only the script, alternating between 👤 Client and 👨‍💻 Developer. Do not include any extra commentary.
"""
