from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.training_model import Training
from cnnClassifier import logger


stage_name = 'Model Training'


class TrainingModelPipeline:
    def __init__(self) -> None:
        pass


    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()



if __name__ == '__main__':
    try:
        logger.info(f'******** Stage  :  {stage_name}  Started ********')
        cal = TrainingModelPipeline()
        cal.main()
        logger.info(f'******** Stage  :  {stage_name}  Completed ********')
    except Exception as e:
        logger.exception(e)
        raise e
