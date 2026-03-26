from validator import data_validation_name, password_validation_name
from storage import Database
from password_generator import create_password
import os

#File functions.
class Manager():
    def __init__(self):
        self.create_db = create_table()
    #Returns the password. 
    def password(self):
        return create_password()
    
    #Gets data from UI stores and validate it.
    def data_validation(self, company, firstname, lastname, password):
        if validate_entry_data(company, firstname, lastname, password):
            Storage().store_data(company, firstname, lastname, password)
            return True
        return False
    
    #Delete data in database
    def delete_data(self, iid, company, firstname, lastname, password):
        Storage().delete_items(iid, company, firstname, lastname, password)

    #Gets database data.
    def database_data(self):
        return Storage().database_data()
    
    #Returns curent path
    def cwd(self):
        return os.path.dirname(__file__)
   
#Class that handels the database.
class Storage():
    #Store data to database.
    def store_data(self, company, firstname, lastname, password):
        if Database().insert_data(company, firstname, lastname, password):
            return True
        else:
            return False

    #Delete items in the database.
    def delete_items(self, iid, company, firstname, lastname, password):
        if Database().delete_item(iid, company, firstname, lastname, password):
            return True
        else:
             return False
    
    #Get data from database.
    def database_data(self):
        data = Database().data_from_database()
        return data

#Validate data
def validate_entry_data(company, firstname, lastname, password):
    if data_validation_name(company) and data_validation_name(firstname) and data_validation_name(lastname):
        if password_validation_name(password):
            return True
        else:
            return False
    else:
        return False

#create table
def create_table():
    try:
        Database().create_table()
        return True
    except:
        return False

#Helper function for database class.

        
print(Manager().cwd())
if __name__ == "__main__":
    ...