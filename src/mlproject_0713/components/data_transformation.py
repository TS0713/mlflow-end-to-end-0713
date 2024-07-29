import os
from mlproject_0713.entity.config_entity import DataTransformationConfig
import pandas as pd
from mlproject_0713 import logger
from sklearn.model_selection import train_test_split

class DataTransformation:
    def __init__(self,config=DataTransformationConfig):
        self.config = config
    
    def train_test_split(self):
        data = pd.read_csv(self.config.data_path)

        train,test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)

        logger.info("Data Splitted into train and test")
        logger.info(f"Train Shape: {train.shape}")
        logger.info(f"Test Shape: {test.shape}")

        print (train.shape)
        print (test.shape)


