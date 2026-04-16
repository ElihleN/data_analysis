
import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
path = os.getenv("PATH")


engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")


df = pd.read_csv(
    path + 'Data/Global_Superstore2.csv',
    encoding='cp1252'
)


df.to_sql(
    name='glob_superstore_data',
    con=engine,
    if_exists='replace',
    index=False
)

print('Loaded successfully')