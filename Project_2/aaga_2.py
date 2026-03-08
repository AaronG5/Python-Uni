import json
from pymongo import MongoClient

def task_2():
   for doc in collection.find():
      print(doc)

def task_3():
   for doc in collection.find(
      {}, {"restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1}
   ):
      print(doc)

def task_4():
   for doc in collection.find(
      {}, {"restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1, "_id": 0}
   ):
      print(doc)

def task_5():
   for doc in collection.find(
      {"borough": "Bronx"}
   ):
      print(doc)

def task_6():
   for doc in collection.aggregate([
      {"$addFields": { 
         "totalScore": { 
            "$sum": "$grades.score"}
      }},
      {"$match": { 
         "$and": [
            {"totalScore": {"$gte": 80}}, 
            {"totalScore": {"$lte": 100}}
         ] 
      }},
   ]):
      print(doc)

def task_7():
   for doc in collection.find().sort([
      ("cuisine", 1),
      ("borough", -1)
   ]):
      print(doc)


# Task 1 {
try:
   client = MongoClient("mongodb://localhost:27017")
   db = client["restaurants_db"]
   collection = db["restaurants"]

   with open("Project_2/restaurants.json") as file:
      for line in file:
         entry = json.loads(line)
         collection.insert_one(entry)
except Exception as e:
   print("Exception occured:", e)
# } Task 1

task_2()
task_3()
task_4()
task_5()
task_6()
task_7()