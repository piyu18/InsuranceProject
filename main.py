from Insurance.logger import logging
from Insurance.exceptions import InsuranceException
from Insurance.utils import get_collection_as_dataframe
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
        get_collection_as_dataframe(database_name='INSURANCE_DATABASE',collection_name='INSURANCE_COLLECTION')
        #test_logger_exception()
    except Exception as e:
        print(e)