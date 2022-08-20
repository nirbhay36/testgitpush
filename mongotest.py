import pymongo
client = pymongo.MongoClient("mongodb+srv://nirbhay36:nirbhay36@nirbhay.knweoit.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d ={"name" : "nirbhay" ,
    "email": "n36" ,
    "surname": "ahir"}

j = [
    {"hi":"hey" ,
    "sk": "kn betho"}
]

database = client['mongotest']
coll = database['test']
##coll.insert_one(d)
coll.insert_many(j)

record = coll.find()
for i in record:
    print(i)

