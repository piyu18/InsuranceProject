import pymongo
import pandas as pd
import json
client = pymongo.MongoClient('mongodb+srv://priya:Priya2508@cluster0.rxtbh.mongodb.net/?retryWrites=true&w=majority')
DATA_FILE_PATH = (r"C:\Users\priya\OneDrive\Desktop\Isurance\InsuranceProject\insurance.csv")
DATABASE_NAME = 'INSURANCE_DATABASE'
COLLECTION_NAME = 'INSURANCE_COLLECTION'

if __name__ == '__main__':
    df = pd.read_csv(DATA_FILE_PATH)
    print(f'Rows and columns:{df.shape}')
    df.reset_index(drop=True,inplace=True)
    print(df.head())
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

