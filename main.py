from cnnClassifier.pipeline.s1_data_ingestion import DataIngestionPipeline
from cnnClassifier.pipeline.s2_prepare_base_model import PrepareBaseModelPipeline
from cnnClassifier.pipeline.s3_training_model import TrainingModelPipeline
from cnnClassifier.pipeline.s4_evaluate_model import EvaluateModelPipeline
from cnnClassifier import logger


logger.info('\n\n\n=====================  Programme Started  =====================\n\n\n')



stage_name = 'Data Ingestion'

try:
    logger.info(f'\n\n******** Stage  =>  {stage_name}  (Started) ********\n\n')
    cal = DataIngestionPipeline()
    cal.main()
    logger.info(f'\n\n******** Stage  =>  {stage_name}  (Completed) ********\n\n')
except Exception as e:
    logger.exception(e)
    raise e




stage_name = 'Prepare Base Model'

try:
    logger.info(f'\n\n******** Stage  :  {stage_name}  (Started) ********\n\n')
    cal = PrepareBaseModelPipeline()
    cal.main()
    logger.info(f'\n\n******** Stage  :  {stage_name}  (Completed) ********\n\n')
except Exception as e:
    logger.exception(e)
    raise e




stage_name = 'Model Training'

try:
    logger.info(f'\n\n******** Stage  :  {stage_name}  (Started) ********\n\n')
    cal = TrainingModelPipeline()
    cal.main()
    logger.info(f'\n\n******** Stage  :  {stage_name}  (Completed) ********\n\n')
except Exception as e:
    logger.exception(e)
    raise e




stage_name = 'Model Evaluation'

try:
    logger.info(f'\n\n******** Stage  :  {stage_name}  (Started) ********\n\n')
    cal = EvaluateModelPipeline()
    cal.main()
    logger.info(f'\n\n******** Stage  :  {stage_name}  (Completed) ********\n\n')
except Exception as e:
    logger.exception(e)
    raise e




logger.info('\n\n\n=====================  Programme Completed  =====================\n\n\n')