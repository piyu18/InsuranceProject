from Insurance.logger import logging
from Insurance.exceptions import InsuranceException
from Insurance.utils import get_collection_as_dataframe
from Insurance.entity import config_entity
from Insurance.entity.config_entity import DataIngestionConfig
import os, sys

def test_logger_exception():
    try:
        logging.info('Starting logging')
        result = 3/0
        print(result)
        logging.info('Ending logging')
    except Exception as e:
        logging.debug(str(e))
        raise InsuranceException(e, sys)



if __name__ == '__main__':
    try:
        #get_collection_as_dataframe(database_name='INSURANCE_DATABASE',collection_name='INSURANCE_COLLECTION')
        #test_logger_exception()
        training_pipeline_config = config_entity.TrainingPipelineConfig()
        data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config = training_pipeline_config)
        print(data_ingestion_config.data_to_dict())
    except Exception as e:
        print(e)