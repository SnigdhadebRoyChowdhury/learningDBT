/*
    In order to see snapshot in action you need to execute the below query
    in the Postgres instance that you have running on your system

    You need to check the ID that you are updating and may have to replace the ID
    if you are loading the data for any other city

*/

UPDATE AIRBNB.RAW_LISTINGS
SET MINIMUM_NIGHTS=30,
updated_at=CURRENT_TIMESTAMP
WHERE ID=2818;