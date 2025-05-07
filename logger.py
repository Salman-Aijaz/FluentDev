# logger.py

import logging

# Create and configure logger
logging.basicConfig(
    level=logging.INFO,
    format="🔍 [%(levelname)s] %(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Get a named logger
logger = logging.getLogger("bidgen")

# Optional: If using in multiple files, you can control this one place
# logger.setLevel(logging.DEBUG)

__all__ = ["logger"]