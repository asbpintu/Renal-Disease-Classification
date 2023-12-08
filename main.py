from cnnClassifier.pipeline.s1_data_ingestion import DataIngestionPipeline
from cnnClassifier.pipeline.s2_prepare_base_model import PrepareBaseModelPipeline
from cnnClassifier.pipeline.s3_training_model import TrainingModelPipeline
from cnnClassifier import logger


logger.info('\n\n\n=====================  Programme Started  =====================\n\n\n')



stage_name = 'Data Ingestion'

try:
    logger.info(f'******** Stage  =>  {stage_name}  (Started) ********')
    cal = DataIngestionPipeline()
    cal.main()
    logger.info(f'******** Stage  =>  {stage_name}  (Completed) ********')
except Exception as e:
    logger.exception(e)
    raise e




stage_name = 'Prepare Base Model'

try:
    logger.info(f'******** Stage  :  {stage_name}  (Started) ********')
    cal = PrepareBaseModelPipeline()
    cal.main()
    logger.info(f'******** Stage  :  {stage_name}  (Completed) ********')
except Exception as e:
    logger.exception(e)
    raise e




stage_name = 'Model Training'

try:
    logger.info(f'******** Stage  :  {stage_name}  (Started) ********')
    cal = TrainingModelPipeline()
    cal.main()
    logger.info(f'******** Stage  :  {stage_name}  (Completed) ********')
except Exception as e:
    logger.exception(e)
    raise e





logger.info('\n\n\n=====================  Programme Completed  =====================\n\n\n')