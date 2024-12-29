from pymongo import MongoClient
import configparser
import pathlib

file_config = pathlib.Path(__file__).parent.parent.parent.joinpath("config.ini")
config = configparser.ConfigParser()
config.read(file_config)

postgres_user = config.get("Postgres", 'USER')
postgres_password = config.get("Postgres", 'PASSWORD')
postgres_name = config.get("Postgres", 'NAME')