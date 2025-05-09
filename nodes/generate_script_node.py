from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from logger import logger
from prompt_templates import meeting_script_prompt
import os   
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

prompt = PromptTemplate.from_template(meeting_script_prompt)

def generate_script_node(state):
    try:
        topic = state.topic
        technical = state.technical
        challenging = state.challenging
        detailed = state.detailed
        budget = state.budget

        # Construct conditional inserts
        technical_note = "🧠 Assume the client is technically knowledgeable." if technical else ""
        challenging_note = "😤 Assume the client is challenging, skeptical, or demanding." if challenging else ""
        detailed_note = "📋 Provide detailed explanations and justifications for each response." if detailed else ""
        budget_note = "💰 Include budget and cost discussions in the conversation." if budget else ""

        final_prompt = prompt.format(
            topic=topic,
            technical_note=technical_note,
            challenging_note=challenging_note,
            detailed_note=detailed_note,
            budget_note=budget_note
        )

        response = llm.invoke(final_prompt)
        logger.info("🧠 Generating concise bid with Gemini...")
        return {"script": response.content}
    except Exception as e:
        logger.exception(f"⚠️ Error in generate_script node: {e}")
        raise
