import sqlalchemy
import pandas as pd
import os
from credentials import get_credentials_from_dbt

def insert_data(project_name: str):
    path = f"{os.getcwd()}/data/listings.csv"
    df = pd.read_csv(path, sep=",")

    df_selected = df[['id', 'listing_url', 'name', 'room_type', 'minimum_nights', 'host_id', 'price']]
    df_selected['price'] = df['price'].str.replace("[$,]", "", regex=True).astype(float)
   
    df_selected['created_at'] = pd.Timestamp.now()
    df_selected['updated_at'] = pd.Timestamp.now()
    # print(df_selected)

    credentials = get_credentials_from_dbt(project_name)
    user = credentials['user']
    passwd = credentials['pass']
    host = credentials['host']
    port = credentials['port']
    database = credentials['dbname']
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{database}"

    engine = sqlalchemy.create_engine(url)
    df_selected.to_sql("raw_listings", engine, schema="airbnb", if_exists="append", index=False)
    print("Data successfully inserted...")

if __name__=="__main__":
    project_name = input("Please enter the dbt project name\n")
    insert_data(project_name)
    