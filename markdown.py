# %% [markdown]
# 

# %% [markdown]
# Import & Connections -----

# %%
import random as rd
import certifi
from pymongo.mongo_client import MongoClient
from ServerDB import Server

# %%
Uri = "mongodb+srv://FelipePalermo:fsrKta0YGh0MPiH4@tarrasque.zslex2g.mongodb.net/?retryWrites=true&w=majority&appName=Tarrasque"
Client = MongoClient(Uri, tlsCAFile=certifi.where())["Server_Database"]


# %% [markdown]
# Functions -----

# %%
def generate_random() : 

    numbers = []
    
    for i in range(0, 4) : 
        numbers.append(rd.randint(1, 6))
    
    menor = min(numbers)
    numbers.remove(menor)
    numbers = sum(numbers)

    return numbers

# %% [markdown]
# Main -----

# %%
class Player : 



    def __init__(self, character_attributes) -> None : 
        

        self.inventory = {}


        if character_attributes != None : 

            self.Guild_ID = character_attributes[0]
            self.Discord_ID = str(character_attributes[1])
            self.Name = character_attributes[2]
            self.Strenght = character_attributes[3]
            self.Dexterity = character_attributes[4]
            self.Constitution = character_attributes[5]
            self.Intelligence = character_attributes[6]
            self.Wisdom = character_attributes[7]
            self.Charisma = character_attributes[8]
            
            self.hp = character_attributes[9] +  self.Constitution

            while True : 
            
                if Server.Check_Exists(self.Guild_ID) >= 1 : 

                    Client[str(self.Guild_ID)].insert_one({
                        "Server_Class" : "Player", 
                        "_id" : self.Discord_ID,
                        "Guild_ID" : self.Guild_ID,
                        "Name" : str(self.Name),  
                        "Hp" : self.hp,
                        "Strenght" : self.Strenght,
                        "Dexterity" : self.Dexterity,
                        "Constitution" : self.Constitution,
                        "Intelligence" : self.Intelligence,
                        "Wisdom" : self.Wisdom,
                        "Charisma" : self.Charisma
                    })

                    break 
                
                else :
                    Server.Create_DB([self.Guild_ID,
                    self.Discord_ID, self.Name])
        else : 
            pass 

    @staticmethod
    def Create_With_Random_Attributes(Guild_ID, Discord_ID) : 
        
        Guild_ID = Guild_ID
        Discord_ID = Discord_ID
        Name = Name
        Strenght = generate_random()
        Dexterity = generate_random()
        Constitution = generate_random()
        Intelligence = generate_random()
        Wisdom = generate_random()
        Charisma = generate_random()

        while True : 
        
            if Server.Check_Exists(Guild_ID) >= 1 : 
                Client[str(Guild_ID)].insert_one({
                    "_id" : Discord_ID,
                    "Guild_ID" : Guild_ID,
                    "Name" : Name,  
                    "Strenght" : Strenght,
                    "Dexterity" : Dexterity,
                    "Constitution" : Constitution,
                    "Intelligence" : Intelligence,
                    "Wisdom" : Wisdom,
                    "Charisma" : Charisma
                })

                break 

            else :
                print("Please, first create a DB to this server!")

# %%
b = Player([10, 115, "Rhuan", 13, 11, 17, 9, 10, 12, 15])

# %%



