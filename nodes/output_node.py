from logger import logger


def output_node(state):
    try:
        logger.info("📝 Meeting Script Generated:")
        logger.info(state.script or "⚠️ No Script found.")
        return state
    except Exception as e:
        logger.exception(f"⚠️ Error in output node: {e}")
        raise