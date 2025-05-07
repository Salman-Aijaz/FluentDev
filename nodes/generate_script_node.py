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
        topic = state["topic"]
        final_prompt = prompt.format(topic=topic)
        response = llm.invoke(final_prompt)
        logger.info("🧠 Generating concise bid with Gemini...")
        return {"script": response.content}
    except Exception as e:
        logger.exception(f"⚠️ Error in generate_script node: {e}")
        raise