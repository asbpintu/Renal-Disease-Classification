from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger

stage_name = 'Data Ingestion'

class DataIngestionPipeline:
    def __init__(self) -> None:
        pass


    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()



if __name__ == '__main__':
    try:
        logger.info(f'******** Stage  :  {stage_name}  Started ********')
        cal = DataIngestionPipeline()
        cal.main()
        logger.info(f'******** Stage  :  {stage_name}  Completed ********')
    except Exception as e:
        logger.exception(e)
        raise e