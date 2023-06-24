from src import logger
from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = 'Data Ingestion stage'
try :
    logger.info(f">>>>>>>> stage {STAGE_NAME} STARTED<<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>>{STAGE_NAME} COMPLETED<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e