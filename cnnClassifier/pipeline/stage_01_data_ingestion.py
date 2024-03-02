from cnnClassifier.config.configuration import Configuration_manager
from cnnClassifier.components.data_ingestion import DataIngestion

from cnnClassifier import logger

STAGE_NAME = "DATA INGESTION STAGE"


class DataIngestionTrainingPipeline():
    def __init__(self):
        pass

    def main(self):
        config = Configuration_manager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()



if __name__=='__main__':
    import os
    print(os.getcwd())
    import sys
    print(sys.executable)
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e