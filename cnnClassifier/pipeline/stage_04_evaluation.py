from cnnClassifier.components.evaluation import Evaluation
from cnnClassifier.config.configuration import Configuration_manager
from cnnClassifier import logger


STAGE_NAME = "Evaluation" 

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        evaluation_config = Configuration_manager()
        val_config = evaluation_config.get_evaluation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()

if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e