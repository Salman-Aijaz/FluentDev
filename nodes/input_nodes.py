from logger import logger

def input_node(topic: str):
    try:
        logger.info("📥 Collecting input...")
        return {"topic": topic}
    except Exception as e:
        logger.exception(f"⚠️ Error in collect_input node: {e}")
        raise