from mlproject_0713.config.configuration import ConfigurationManager
from mlproject_0713.components.model_trainer import ModelTrainer
from mlproject_0713 import logger
from pathlib import Path

STAGE_NAME = "Model Trainer"

class ModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config = model_trainer_config)
        model_trainer.train()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<<\n\nx================x")
    except Exception as e:
        logger.exception(e)
        raise e

