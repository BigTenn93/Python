from dbm import _Database
from mysqlconnections import connectToMySQL

class Dog:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.breed = data['breed']
        self.color = data['color']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query + "SELECT * FROM dogs;"
        results = connectToMySQL(DATABASE).query_db(query)
        #print(results)
        all_dogs = []
        for row_from_db in results:
            dog_instance = cls(row_from_db) #instantiates dog object