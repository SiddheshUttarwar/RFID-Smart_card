import pymongo

class FoodMenu :

    def __init__ (self):
        Client = pymongo.MongoClient("mongodb://localhost:27017")
        self.database = Client.get_database("VNRVJIET")
        self.collections = self.database.get_collection("MENU")

    def insert_data(self,id,dish,price):
        self.id = id
        self.dish = dish
        self.price = price

        document = {
            'id' : self.id,
            'dish' : self.dish,
            'price':self.price
        }

        self.collections.insert_one(document)


    def get_table(self):
        self.documents = self.collections.find({})

        return self.documents

    def delete_data(self,id):
        query = {'id':id}
        self.collections.delete_one(query)










