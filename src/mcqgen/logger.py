import logging
import os
from datetime import datetime

# Create log file name with current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create logs directory if it doesn't exist
log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path, exist_ok=True)

# Full path to the log file
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Changed to logging.INFO
    filename=LOG_FILEPATH,  # Corrected to use the full path
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)

