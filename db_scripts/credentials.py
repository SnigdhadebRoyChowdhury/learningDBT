import os
import yaml

def get_credentials_from_dbt(project_name: str):
    
    profile_path = os.environ.get('HOME') +'/.dbt/profiles.yml'
    with open(profile_path, 'r') as f:
        credentials = yaml.safe_load(f)

    return credentials[project_name]['outputs']['dev']