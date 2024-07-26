
import certifi
from pymongo.mongo_client import MongoClient

Uri = "mongodb+srv://FelipePalermo:fsrKta0YGh0MPiH4@tarrasque.zslex2g.mongodb.net/?retryWrites=true&w=majority&appName=Tarrasque"
Client = MongoClient(Uri, tlsCAFile=certifi.where())["Server_Database"]

class Server : 
    
    def __init__(self, list_with_attributes) -> None : 
        

        self.Guild_ID = str(list_with_attributes[0])

        self.DB_Creator_ID = str(list_with_attributes[1])
        self.DB_Creator_Name = str(list_with_attributes[2])

        self.Creator_Data = self.DB_Creator_Name + " : " + self.DB_Creator_ID

        if Client[self.Guild_ID].count_documents({"_id" : self.Guild_ID}) : 
            pass 

        else : 
            Client[self.Guild_ID].insert_one({
                "Data_Class" : "Server Database", 
                "_id" : self.Guild_ID,
                "Database created by" : self.Creator_Data,
                "Language" : "Pt-Br",
                "D&D Version" : "5e",
                "Allow Homebrew" : False})

    @staticmethod
    def Create_DB(List_of_Attributes) -> None : 

        Guild_ID = str(List_of_Attributes[0])

        DB_Creator_ID = str(List_of_Attributes[1])
        DB_Creator_Name = str(List_of_Attributes[2])

        Creator_Data = DB_Creator_Name + " : " + DB_Creator_ID

        if Client[Guild_ID].count_documents({"_id" : Guild_ID}) >= 1 : 
            pass 

        else : 
            Client[Guild_ID].insert_one({
                "_id" : Guild_ID,
                "Server_Class" : "Server Database", 
                "Database created by" : Creator_Data,
                "Language" : "Pt-Br",
                "D&D Version" : "5e",
                "Allow Homebrew" : False})


    @staticmethod 
    def Change_Language(GuildID, Language) -> None : 

        if Language == "En-Us" :
            Client[str(GuildID)].update_one({"_id" : str(GuildID)}, {"$set" : {"Language" : "En-Us"}})
        
        if Language == "Pt-Br" :
            Client[str(GuildID)].update_one({"_id" : str(GuildID)}, {"$set" : {"Language" : "Pt-Br"}})

    @staticmethod
    def Check_Exists(GuildID) -> bool :
        if Client[str(GuildID)].count_documents({"_id" : str(GuildID)}) >= 1 : 
            return True 
        else : 
            return False 