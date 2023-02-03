import logging
from datetime import datetime
import os

LOG_DIR = "Insurance_log"

CURRENT_TIMESTAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

LOG_FILE = f"log_{CURRENT_TIMESTAMP}.log"

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE)

logging.basicConfig(filename=LOG_FILE_PATH,
                    level=logging.DEBUG,
                    filemode='w',
                    format='[%(asctime)s] %(name)s %(levelname)s %(message)s',
                    )