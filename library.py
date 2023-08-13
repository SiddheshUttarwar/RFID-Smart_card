import pymongo

class Library:

    def __init__(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        self.database = client.get_database("VNRVJIET")
        self.collections = self.database.get_collection("LIBRARY")

    def insert_book(self,_ID,book_name):
        self._ID = _ID
        self.book_name = book_name

        document = {
            '_id' : self._ID,
            'book_name' : self.book_name
        }

        if document not in self.collections.find({}):
            self.collections.insert_one(document)


    def get_library(self):
        self.documents = self.collections.find({})

        return self.documents

    def delete_book(self,id):
        query = {'_ID' : id}
        self.collections.delete_one(query)





library = Library()
library.insert_book(1243, "Introduction to Vlsi design")
library.insert_book(4354 , "Basics of frontend development")
library.insert_book(7331, "Advanced Signal Processing")
library.insert_book(8876, "Fundamentals of IOT")
library.insert_book(9065 , "Digital Image Processing")
library.insert_book(6754 , "Computer Networks and networking fundamnetals")


