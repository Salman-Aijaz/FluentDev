meeting_script_prompt = """
You're simulating a 30-minute meeting between a 👤 Client and a 👨‍💻 Developer.

📝 Topic: {topic}

🎯 Goal: Generate a realistic back-and-forth conversation that spans approximately a 30-minute meeting. Include multiple follow-up questions, clarifications, and answers. Ensure both client and developer go in-depth about requirements, timelines, costs, and features.

Example:
👤 Client:
That's helpful. When do charges start to apply?

👨‍💻 Developer:
Charges begin when:

✅ Output only the script, alternating between 👤 Client and 👨‍💻 Developer. Do not include any extra commentary.
"""
