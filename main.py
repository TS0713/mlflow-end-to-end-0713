"""
from src.mlproject_0713 import logger
logger.info("Hello World!! custom logging")
"""

from mlproject_0713.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlproject_0713 import logger

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<<\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e
