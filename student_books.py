import pymongo

class Student_Books:

    def __init__(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        self.database = client.get_database("VNRVJIET")
        self.collections = self.database.get_collection("STUDENT_BOOKS")

    def add_data(self,student_id,books):
        self.student_id = student_id
        self.books = books

        document ={
            '_id' : self.student_id,
            'books':self.books
        }
        if document not in self.collections.find({}):
            self.collections.insert_one(document)

    