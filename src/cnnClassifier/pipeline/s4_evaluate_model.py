from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.evaluate_model import Evaluation
from cnnClassifier import logger



stage_name = 'Model Evaluation'


class EvaluateModelPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()



if __name__ == '__main__':
    try:
        logger.info(f'******** Stage  :  {stage_name}  Started ********')
        cal = EvaluateModelPipeline()
        cal.main()
        logger.info(f'******** Stage  :  {stage_name}  Completed ********')
    except Exception as e:
        logger.exception(e)
        raise e