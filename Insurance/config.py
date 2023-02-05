import pandas as pd
import numpy as np
import pymongo
import os, sys
import json
from dataclasses import dataclass

@dataclass
class EnvironmentVariable():
    mongo_db_url = os.getenv("MONGO_DB_URL")

env_variable = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_variable.mongo_db_url)
TARGET_COLUMN = 'expenses'
print(env_variable.mongo_db_url)