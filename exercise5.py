import pymongo
#create db
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongo_client["mydatabase"]
col = db["customers"]
#insert records
records = [{"name":"Kyle","student_id":"303", "hw1":50}, {"name":"Chris","student_id":"101", "hw1":10}, {"name":"Ann","student_id":"301", "hw1":80} , {"name":"Tim","student_id":"305", "hw1":99} , {"name":"Joe","student_id":"306", "hw1":67} , {"name":"Nick","student_id":"307", "hw1":2}]
x = col.insert_many(records)
# query - search for ‘Stef
name_query = { "name":"Stef"}
print(col.count_documents({}))
stef_record = col.find()
list1 = []
for x in stef_record:
    print(x.get('name'),x.get('hw1'))
    if x.get('hw1') is not None and x.get('hw1') > 50:
        list1.append(x.get('name'))

print(list1)