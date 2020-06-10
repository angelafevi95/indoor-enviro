from pymongo import MongoClient

class mongoDB():

    def __init__(self):
        self.myDB       = "mongodb+srv://pi:N0tT0Kn0w@cluster0-wegmd.mongodb.net/test?retryWrites=true&w=majority"
        self.DBclient   = MongoClient(self.myDB)
        self.db         = self.DBclient.get_database('sensors_db')
        self.records    = db.sensors_record

    # def getCollection(self):  
    #     # Be carefull by writing the exact name of the collection. 
    #     db              = self.DBclient.get_database('sensors_db')
    #     records         = db.sensors_record
    #     return records   

    ## To check the count of documents I have currently in my collection
    def getCountDocs(self, records):
        # We can provide a filter or not insede de {}
        count =  records.count_documents({})
        return count 
    
    ## Get all the documents of the collection at a time
    def importData(self, records):
        list(records.find())
    
    # ## Get one document of the collection by filtering per key
    # def importDataKey(self, records):
    #     records.find_one({'key': value})


    ##Push data to MondoDB
    # def updateDocument(self, records):
        ##Funtion used to modify an entry on an existing Document 

    ## Create a def on main() RPI to create a dictionary using the information provided by the sensors. 
    def exportData(self, dicctionary, records):
        records.insert_one(dicctionary)
        # Si uso records.insert_many(dictList) exporto casa diccionario dentro de la lista como un nuevo document. 
        # Es mejor, para un dia envira un diccionario de listas y no una lisya de diccionarios ej: "mq2' = 3,4,4 "
        


    
