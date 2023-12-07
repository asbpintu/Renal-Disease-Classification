from cnnClassifier.pipeline.s1_data_ingestion import DataIngestionPipeline
from cnnClassifier import logger


stage_name = 'Data Ingestion'


try:
    logger.info(f'******** Stage  =>  {stage_name}  (Started) ********')
    cal = DataIngestionPipeline()
    cal.main()
    logger.info(f'******** Stage  =>  {stage_name}  (Completed) ********')
except Exception as e:
    logger.exception(e)
    raise e