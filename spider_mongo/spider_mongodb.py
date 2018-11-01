import pymongo


client = pymongo.MongoClient(host='localhost', port=27017)

db = client.test_mongo

collection = db.students

student1 = {
    'id': '2015442332',
    'name': 'xiaoluoge',
    'age': 22,
    'gender': 'male',
}

student2 = {
    'id': '2015442333',
    'name': 'haha',
    'age': 22,
    'gender': 'male',
}
student3 = {
    'id': '2015442334',
    'name': 'lala',
    'age': 22,
    'gender': 'male',
}
student4 = {
    'id': '2015442335',
    'name': 'goudan',
    'age': 23,
    'gender': 'male',
}
student5 = {
    'id': '2015442336',
    'name': 'xiaoming',
    'age': 24,
    'gender': 'male',
}
student6 = {
    'id': '2015442337',
    'name': 'soulmate',
    'age': 25,
    'gender': 'male',
}

# 插入多条数据
# result = collection.insert_many([student4, student5, student6])
# print(result)
# print(result.inserted_ids)
# print('*'*20)

# 查询数据
result1 = collection.find()
print(type(result1))   #返回的是生成器
print(result1)
print('*'*20)

result2 = collection.find_one({'name': 'haha'})
print(type(result2))    #返回的是字典
print(result2)
print('*'*20)

# result3 = collection.find_one({'_id': ObjectId('5bd9225bc57db403e5ad6f81')})
# print(type(result3))   #返回的是字典
# print(result3)
# print('*'*20)

# 多条数据查询
results = collection.find({'age': 22})
print(type(results))   #返回的是一个生成器
for result in results:
    print(result)
print('*'*30)

# 查询年龄大于22的数据
results = collection.find({'age':{'$gt': 22}})
print(type(results))
for result in results:
    print(result)
print('*'*20)

# 统计有多少条数据
count = collection.find().count()
print(count)
print('*'*40)





