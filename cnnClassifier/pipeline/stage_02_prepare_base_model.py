from cnnClassifier import logger
from cnnClassifier.config.configuration import Configuration_manager
from cnnClassifier.components.prepare_base_model import  PrepareBaseModel


STAGE_NAME = "PrePareBaseModel Training Pipeline"

class PrepareBaseModelTraningPipeline:
    def __init__(self):
        pass

    def main(self):
        config = Configuration_manager()
        prepare_base_model_config = config.get_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTraningPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e