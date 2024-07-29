"""
from src.mlproject_0713 import logger
logger.info("Hello World!! custom logging")
"""

from mlproject_0713.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlproject_0713.pipeline.stage_02_data_validation import DataValidationPipeline
from mlproject_0713.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlproject_0713.pipeline.stage_04_model_trainer import ModelTrainingPipeline
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

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<<\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<<\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f">>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<<\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e