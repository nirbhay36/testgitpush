import pymongo
client = pymongo.MongoClient("mongodb+srv://nirbhay36:nirbhay36@nirbhay.knweoit.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d ={"name" : "nirbhay" ,
    "email": "n36" ,
    "surname": "ahir"}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

