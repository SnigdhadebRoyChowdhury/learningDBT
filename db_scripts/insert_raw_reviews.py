import sqlalchemy
import pandas as pd
import os

# def insert_data(db: str, user: str, passwd: str)
def insert_data():
    path = f"{os.getcwd()}/data/listings.csv"
    df = pd.read_csv(path, sep=",")

    df_selected = df[['id', 'listing_url', 'name', 'room_type', 'minimum_nights', 'host_id', 'price']]
   
    df_selected['created_at'] = pd.Timestamp.now()
    df_selected['updated_at'] = pd.Timestamp.now()
    print(df_selected)

    # url = f"postgresql://{user}:{passwd}@localhost:5432/{db}"
    # engine = sqlalchemy.create_engine(url)
    # df_selected.to_sql("raw_listings", engine, schema="airbnb", if_exists="append", index=False)
    # print("Data successfully inserted...")

if __name__=="__main__":
    # db = input("Please enter the database name\n")
    # user = input("Please enter the username\n")
    # passwd = input("Please enter your password\n")
    # insert_data(db, user, passwd)
    insert_data()