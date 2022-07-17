import pymongo
client = pymongo.MongoClient("mongodb+srv://root:localhost@cluster0.esvnakk.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

# client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
# db = client.test
# print(db)


d = {
    "name" : "ankur",
    "email" : "ank@example.com",
    "surname" : "kumar"
}

db1=client['mongotest']
coll=db1['test1']
coll.insert_one(d)