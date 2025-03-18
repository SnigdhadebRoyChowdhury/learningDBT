import os
import yaml
import sqlalchemy

def get_credentials_from_dbt(project_name: str):
    
    profile_path = os.environ.get('HOME') +'/.dbt/profiles.yml'
    with open(profile_path, 'r') as f:
        credentials = yaml.safe_load(f)

    credential =  credentials[project_name]['outputs']['dev']
    user = credential['user']
    passwd = credential['pass']
    host = credential['host']
    port = credential['port']
    database = credential['dbname']
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{database}"
    return url 