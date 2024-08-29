import logging
import os
from datetime import datetime

# Generate the log file name based on current datetime
log_filename = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the path for log files
logs_directory = os.path.join(os.getcwd(), 'logs')

# Ensure the 'logs' directory exists
os.makedirs(logs_directory, exist_ok=True)

# Full path for the log file
log_file_path = os.path.join(logs_directory, log_filename)

# Configure the logging
logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s-%(levelname)s-%(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")
