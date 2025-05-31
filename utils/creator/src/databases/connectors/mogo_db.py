from pymongo import MongoClient 
# Connexion à la base de données MongoDB
client = MongoClient('localhost', 27017)
db = client['example']
collection = db['users']

# Insertion de données dans la collection
collection.insert_one({'name': 'Alice', 'age': 30})
collection.insert_one({'name': 'Bob', 'age': 25})
