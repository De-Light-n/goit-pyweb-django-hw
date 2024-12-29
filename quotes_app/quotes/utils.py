from pymongo import MongoClient
import configparser
import pathlib

file_config = pathlib.Path(__file__).parent.parent.parent.joinpath("config.ini")
config = configparser.ConfigParser()
config.read(file_config)
mongo_user = config.get('MongoDB', 'USER')
mongodb_pass = config.get('MongoDB', 'PASS')
mongo_domain = config.get('MongoDB', 'DOMAIN')
mongo_client = MongoClient(host=f"mongodb+srv://{mongo_user}:{mongodb_pass}@{mongo_domain}/")

def get_mongodb():
    db = mongo_client.authors_and_quotes
    return db


    
