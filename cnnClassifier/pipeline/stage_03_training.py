from cnnClassifier import logger
from cnnClassifier.components.training import Training
from cnnClassifier.config.configuration import Configuration_manager
from cnnClassifier.config.configuration import TrainingConfig
from cnnClassifier.components.prepare_callbacks import PrepareCallbacks

STAGE_NAME = "Training pipeline"

class TrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = Configuration_manager()
        prepare_callbacks_config = config.prepare_callback_config()
        prepare_call_backs = PrepareCallbacks(config=prepare_callbacks_config)
        callbacks = prepare_call_backs.get_tb_ckpt_callbacks()

        training_config = config.get_training_config()
        training        = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(callback_list=callbacks)


if __name__=='__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = TrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
        
