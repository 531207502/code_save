import pymongo
client=pymongo.MongoClient(host="localhost",port=27017)
db=client.test
collection1=db.test1
dict1={"abc":"123"}
collection1.insert_one({"bcd":"2341","name":"cyl","age":"32"})
print(client.db)
result=collection1.find_one()
result2=collection1.find_one({"age":"22"})
result3=collection1.find({"name":"cyl"})
print(list(collection1.find()))
print(result)
print(result2)
print(list(result3))
print(type(result))
print(result.keys())
filter
