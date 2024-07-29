from mlproject_0713.config.configuration import ConfigurationManager
from mlproject_0713.components.data_validation import DataValidation
from mlproject_0713 import logger

STAGE_NAME = "Data Validation"

class DataValidationPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__=="__main__":
    try:
        logger.info(f">>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<<\n\nx================x")
    except Exception as e:
        logger.exception(e)
        raise e
