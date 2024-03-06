from cnnClassifier.constants import *
from cnnClassifier.utils.common import create_directories,read_yaml
from cnnClassifier.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig,PrepareCallbackConfig,TrainingConfig,EvaluationConfig
from cnnClassifier import logger
import os
import yaml
class Configuration_manager:
    def __init__(self,
            config_file_path = CONFIG_FILE_PATH,
            params_file_path = PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_file_path=config.local_file_path,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    

    def get_base_model_config(self) -> PrepareBaseModelConfig:
        model_params = self.config.prepare_base_model
        create_directories([model_params.root_dir])
        base_model_config  = PrepareBaseModelConfig(
            root_dir=model_params.root_dir,
            base_model_path=model_params.base_model_path,
            updated_base_model_path=model_params.updated_base_model_path,
            params_image_size= self.params.IMAGE_SIZE,
            params_include_top= self.params.INCLUDE_TOP,
            model_weights = self.params.WEIGHTS,
            model_classes = self.params.CLASSES,
            learning_rate = self.params.LEARNING_RATE,
        )
        return base_model_config
    
    def prepare_callback_config(self) -> PrepareCallbackConfig:
        config  = self.config.prepare_callbacks
        create_directories([config.root_dir])
        call_back_config = PrepareCallbackConfig(
            root_dir=config.root_dir,
            tensorboard_root_log_dir=config.tensorboard_root_log_dir,
            checkpoint_model_file_path=config.checkpoint_model_filepath
        )
        return call_back_config
    

    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        params  = self.params
        create_directories([training.root_dir])
        prepare_base_model = self.config.prepare_base_model
        training_config = TrainingConfig(
            root_dir=training.root_dir,
            trained_model_path=training.trained_model_path,
            updated_base_model_path=prepare_base_model.updated_base_model_path,
            training_data=os.path.join(self.config.data_ingestion.unzip_dir,"Chicken-fecal-images"),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )

        return training_config
    
    def get_evaluation_config(self) -> EvaluationConfig:
        eval_config = EvaluationConfig(
            path_of_model=Path("artifacts/training/model.h5"),
            training_data=Path("artifacts/data_ingestion/Chicken-fecal-images"),
            all_params=self.params,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE
        )
        return eval_config
