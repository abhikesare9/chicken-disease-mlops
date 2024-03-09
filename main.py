from cnnClassifier import logger
import shutil
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTraningPipeline
from cnnClassifier.pipeline.stage_03_training import TrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline


STAGE_NAME = "Data Ingestion stage"
try:
   shutil.rmtree('artifacts')
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "PrePare Base Model"
try: 
      logger.info(f">>>>>>>>STAGE {STAGE_NAME} started<<<<<<<<<<<<<")
      prepare_base_model = PrepareBaseModelTraningPipeline()
      prepare_base_model.main()
      logger.info(f">>>stage {STAGE_NAME} completed<<<<<<")
except Exception as e:
      logger.exception(e)
      raise


STAGE_NAME = "Training pipeline"
try: 
      logger.info(f">>>>>>>>STAGE {STAGE_NAME} started<<<<<<<<<<<<<")
      training_model = TrainingPipeline()
      training_model.main()
      logger.info(f">>>stage {STAGE_NAME} completed<<<<<<")
except Exception as e:
      logger.exception(e)
      raise


STAGE_NAME = "Evaluation pipeline"
try:
       logger.info(f">>>>>>>>STAGE {STAGE_NAME} started<<<<<<<<<<<<<")
       evaluation_pipeline = EvaluationPipeline()
       evaluation_pipeline.main()
       logger.info(f">>>stage {STAGE_NAME} completed<<<<<<")
except Exception as e:
      logger.exception(e)
      raise
       
