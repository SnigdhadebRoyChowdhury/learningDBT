import sqlalchemy
import pandas as pd
import os
from credentials import get_credentials_from_dbt

def insert_data(project_name: str):
    path = f"{os.getcwd()}/data/listings.csv"
    df = pd.read_csv(path, sep=",")

    df_selected = df[['host_id', 'host_name', 'host_is_superhost']]
    df_selected['created_at'] = pd.Timestamp.now()
    df_selected['updated_at'] = pd.Timestamp.now()
    df_selected = df_selected.rename(columns={'host_id':'id', 'host_name':'name','host_is_superhost':'is_superhost'})
    # print(df_selected)

    url = get_credentials_from_dbt(project_name)
    engine = sqlalchemy.create_engine(url)
    df_selected.to_sql("raw_hosts", engine, schema="airbnb", if_exists="append", index=False)
    print("Data successfully inserted...")

if __name__=="__main__":
    project_name = input("Please enter the dbt project name\n")
    insert_data(project_name)
    