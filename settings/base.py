import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv('.env')

MASTER_DB_NAME=os.getenv('MASTER_DB_NAME')
MASTER_DB_USER=os.getenv('MASTER_DB_USER')
MASTER_DB_PASSWORD=os.getenv('MASTER_DB_PASSWORD')
MASTER_DB_HOST=os.getenv('MASTER_DB_HOST')