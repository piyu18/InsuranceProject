import pandas as pd
import numpy as np
import os
import sys
from Insurance.exceptions import InsuranceException
from Insurance.logger import logging
from Insurance.config import mongo_client

def get_collection_as_dataframe(database_name:str, collection_name:str)->pd.DataFrame:
    try:
        #print("Database",database_name,collection_name)
        logging.info(f"Reading data from database: {database_name} and collection: {collection_name}")
        df = pd.DataFrame(mongo_client[database_name][collection_name].find())
        #print(df.columns)
        logging.info(f"Columns in df: {df.columns}")
        if '_id' in df.columns:
            logging.info(f"Dropping id column")
            df.drop('_id', axis=1, inplace=True)
        logging.info(f"Rows & columns in df: {df.shape}")
        return df
    except Exception as e:
        raise InsuranceException(e, sys)

#get_collection_as_dataframe(database_name='INSURANCE_DATABASE',collection_name='INSURANCE_COLLECTION')