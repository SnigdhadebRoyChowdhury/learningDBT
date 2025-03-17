import sqlalchemy
import pandas as pd
import os
from credentials import get_credentials_from_dbt


def insert_data(project_name: str):
    path = f"{os.getcwd()}/data/reviews.csv"
    df = pd.read_csv(path, sep=",")

    df_selected = df[['listing_id', 'date', 'reviewer_name', 'comments']]
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
    df_selected.to_sql("raw_reviews", engine, schema="airbnb", if_exists="append", index=False)
    print("Data successfully inserted...")

if __name__=="__main__":
    project_name = input("Please enter the dbt project name\n")
    insert_data(project_name)
    