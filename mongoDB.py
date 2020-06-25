from pymongo import MongoClient

##To check:
# https://www.mongodb.com/presentations/best-practices-for-working-with-iot-and-time-series-data

class mongoDB():

    """
This class is defined to manage MongoDB Atlas access and data. 

Atributes: 
    #   Variables:

    * myDB: 
    As per provider descrption DataBase URL format depends on the Python verssion used and it purpose. 
    In this case, at least Python 3.6 should be used. 

    * DBCLient:
    Pymongo object used to connect myDB

    * DB: 
    DataBase selected among the existing ones on the cluster. 

    * Records: 
    Once the DB is selected, we choose the record per USER. This way we do not mix up information related to different users.

     #  Funtions: 
    * getcollection:
    INPUT: none
    OUTPUT: Given a chosen Database returns a collection. 

    * getCountDocs:
    INPUT: collection name
    OUTPUT: Number of existing documents in a collection
    
    * importData: 
    INPUT: collection name
    OUTPUT: a lists containing all the documents of the collection at a time

    * exportData:
    INPUT: dictionary to be added to a collection, collection name
    OUTPUT: none 

    """

    def __init__(self):

        ## URL to connect Python API to MongoDB Atlas 
        self.myDB       = "mongodb+srv://pi:N0tT0Kn0w@cluster0-wegmd.mongodb.net/test?retryWrites=true&w=majority"
        self.DBclient   = MongoClient(self.myDB)
        self.db         = self.DBclient.get_database('sensors_db')
        self.records    = self.db.Angela_DB

    def getCollection(self):  
        # Be carefull by writing the exact name of the collection. 
        db              = self.DBclient.get_database('sensors_db')
        records         = db.sensors_record
        return records   

    def getCountDocs(self, records):
        # We can provide a filter or not inside de {}
        count =  records.count_documents({})
        return count 
    
    def importData(self, records):
        list(records.find())

    def exportData(self, dicctionary, records):
        records.insert_one(dicctionary)
    
    # ## Get one document of the collection by filtering per key
    # def importDataKey(self, records):
    #     records.find_one({'key': value})

    ##Push data to MondoDB
    # def updateDocument(self, records):
        ##Funtion used to modify an entry on an existing Document 


        
        


    
