import pymongo
import gridfs

class student_data:
    
    def __init__(self):
        client = pymongo.MongoClient('mongodb://localhost:27017')
        self.database = client.get_database("VNRVJIET")
        self.collections = self.database.get_collection("Student_data")

    def insert_data(self,_ID,rollno,name,email,phone,resume):
        self._ID = _ID
        self.rollno = rollno
        self.name = name
        self.email = email
        self.phone = phone
        self.resume = resume

        document = {'_id':self._ID,
                    'rollno':self.rollno,
                    'name':self.name,
                    'email':self.email,
                    'Phone':self.phone,
                    'resume': self.resume
                   }

        self.collections.insert_one(document)

    def get_Details(self,_ID):
        self.ID = _ID
        self.data = self.collections.find_one({'_id':self.ID},{'_id':0})
        return self.data

    def get_name(self,_ID):
        self.ID = _ID
        self.data = self.collections.find_one({'_id':self.ID},{'_id':0})
        return self.data['name']

    def get_rollno(self,_ID):
        self.ID = _ID
        self.data = self.collections.find_one({'_id':self.ID},{'_id':0})
        return self.data['rollno']

    def get_phone(self,_ID):
        self.ID = _ID
        self.data = self.collections.find_one({'_id':self.ID},{'_id':0})
        return self.data['Phone']
    
    def get_documents(self,_ID):
        self.ID = _ID
        self.data = self.collections.find_one({'_id':self.ID},{'_id':0})
        resume = self.data['resume']
        return resume


    def update_name(self,_ID,new_name):
        self.ID = _ID
        prev = {"_id":self.ID}
        self.new_name = new_name
        nextt = {"$set":{"name":self.new_name}}
        self.collections.update_one(prev,nextt)

    def update_rollno(self,_ID,new_rollno):
        self.ID = _ID
        prev = {"_id":self.ID}
        self.new_rollno = new_rollno
        nextt = {"$set":{"rollno":self.new_rollno}}
        self.collections.update_one(prev,nextt)

    def update_phone(self,_ID,new_phone):
        self.ID = _ID
        prev = {"_id":self.ID}
        self.new_phone = new_phone
        nextt = {"$set":{"phone":self.new_phone}}
        self.collections.update_one(prev,nextt)

    def update_email(self,_ID,new_email):
        self.ID = _ID
        prev = {"_id":self.ID}
        self.new_email = new_email
        nextt = {"$set":{"phone":self.new_email}}
        self.collections.update_one(prev,nextt)

    def update_resume(self,_ID,new_resume):
        self.ID = _ID
        prev = {"_id":self.ID}
        self.new_resume = new_resume
        nextt = {"$set":{"resume":self.new_resume}}
        self.collections.update_one(prev,nextt)