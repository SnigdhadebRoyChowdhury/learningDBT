import sqlalchemy
import pandas as pd
from credentials import get_credentials_from_dbt
from pathlib import Path


def insert_data(project_name: str):
    parent_path = Path.cwd().parent
    path = f"{parent_path}/data/reviews.csv"
    df = pd.read_csv(path, sep=",")

    df_selected = df[['listing_id', 'date', 'reviewer_name', 'comments']]
    df_selected['created_at'] = pd.Timestamp.now()
    df_selected['updated_at'] = pd.Timestamp.now()
    # print(df_selected)
    
    url = get_credentials_from_dbt(project_name)
    
    engine = sqlalchemy.create_engine(url)
    df_selected.to_sql("raw_reviews", engine, schema="airbnb", if_exists="append", index=False)
    print("Data successfully inserted...")

if __name__=="__main__":
    project_name = input("Please enter the dbt project name\n")
    insert_data(project_name)
    