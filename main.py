from Insurance.logger import logging
from Insurance.exceptions import InsuranceException
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
        test_logger_exception()
    except Exception as e:
        print(e)