import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"


log_filename = "running_logs.log"

log_filepath = os.path.join(os.getcwd(),"logs",log_filename)

os.makedirs(os.path.join(os.getcwd(),"logs"), exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# initiaing the logging specify some name - can be any name

logger = logging.getLogger("mlProjectLogger")


