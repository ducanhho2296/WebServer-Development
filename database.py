from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://<username>:<password>@cluster0.yp7wi6x.mongodb.net/sample_mflix?retryWrites=true&w=majority"

client = MongoClient(uri)

def get_database():
    return client['sample_mflix']


if __name__ == "__main__":
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        print("\n\n------------------------------------------------\n\n")
        print(client.list_database_names())
        print("\n\n------------------------------------------------\n\n")
        print(client.get_database("sample_mflix").list_collection_names())

    except Exception as e:
        print(e)