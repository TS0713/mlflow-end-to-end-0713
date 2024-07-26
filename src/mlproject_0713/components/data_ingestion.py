import os
from urllib.request import urlretrieve
import zipfile
from mlproject_0713 import logger
from mlproject_0713.utils.common import get_size
from pathlib import Path
from mlproject_0713.entity.config_entity import DataIngestionConfig



class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config 
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
                )
            logger.info(f"{filename} download! with following info: \{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
    
    def extract_zip_file(self):
        """
        zipe_file_path: str
        Extracts Zip File into data directory
        Function return None
        """
        unzip_path = Path(self.config.unzip_dir)
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
