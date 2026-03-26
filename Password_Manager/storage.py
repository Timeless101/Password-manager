import sqlite3


class Database():
    #Check connection.
    def verified_connection(self):
        try:
            con = sqlite3.connect("Password.db")
            con.close()
            return True
        except sqlite3.DatabaseError:
            print("could not connect to database")
            return False
        
    #Create table.
    def create_table(self):
        try:
            con, c = open_connection()
            table_creation = """
            CREATE TABLE IF NOT EXISTS password (
	        Id INTEGER PRIMARY KEY,
            Company TEXT NOT NULL,
   	        Firstname TEXT NOT NULL,
	        Lastname TEXT NOT NULL,
	        Password TEXT NOT NULL
            );
            """
            c.execute(table_creation)
            con.commit()
            c.close()
            con.close()
            return True
        except:
            return False

    #View the rows.
    def data_from_database(self):
        try:
            con, c = open_connection()
            view = """SELECT * FROM PASSWORD"""
            c.execute(view)
            rows = c.fetchall()
            c.close()
            con.close()
            return rows
        except:
            return False

    #Insert data into table.
    def insert_data(self, company, firstname, lastname, password):
        try:
            con, c = open_connection()
            con.execute("INSERT INTO password (Company, Firstname, Lastname, Password) VALUES (?,?,?,?)",(company, firstname, lastname, password))
            con.commit()
            c.close()
            con.close()
            return True
        except:
            c.close()
            con.close()
            return False

    #Delete data from database.
    def delete_item(self, iid, company, fistname, lastname, password):
        try:    
            con, c = open_connection()
            c.execute("DELETE FROM password WHERE (Id, Company, Firstname, Lastname, Password) = (?,?,?,?,?)", (iid, company, fistname, lastname, password))
            con.commit()
            c.close()
            con.close()
            return True
        except:
            return False

#Connection helper.
def open_connection():
    con = sqlite3.connect("Password.db")
    c = con.cursor()
    return (con, c)

if __name__ == "__main__":
    ...