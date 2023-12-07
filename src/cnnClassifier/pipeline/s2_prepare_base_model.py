from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger



stage_name = 'Prepare Base Model'

class PrepareBaseModelPipeline:
    def __init__(self) -> None:
        pass


    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()



if __name__ == '__main__':
    try:
        logger.info(f'******** Stage  :  {stage_name}  Started ********')
        cal = PrepareBaseModelPipeline()
        cal.main()
        logger.info(f'******** Stage  :  {stage_name}  Completed ********')
    except Exception as e:
        logger.exception(e)
        raise e