import os
import pymongo

ENVIRONMENT = os.environ["ENVIRONMENT"]
if ENVIRONMENT == "local":
    connection_string = "mongodb://localhost:27017"
    DB_NAME = "billing_system"
else:    
    MONGO_CLUSTER = os.environ["MONGO_URI"]
    MONGO_USERNAME = os.environ["MONGO_USERNAME"]
    MONGO_PASSWORD = os.environ["MONGO_PASSWORD"]
    DB_NAME = os.environ["DB_NAME"]
    connection_string = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_CLUSTER}/?retryWrites=true&ssl=true&ssl_cert_reqs=CERT_NONE&w=majority"


db_client = pymongo.MongoClient(connection_string)
db_client = db_client.get_database(DB_NAME)

products_collection = db_client['products']
invoices_collection = db_client['invoices']
users_collection = db_client['users']