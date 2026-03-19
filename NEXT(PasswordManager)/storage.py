import sqlite3

#check connection
def verified_connection():
    try:
        con = sqlite3.connect("Password.db")
        con.close()
        return True
    except sqlite3.DatabaseError:
        print("could not connect to database")
        return False
    
#Connection helper
def open_connection():
    con = sqlite3.connect("Password.db")
    c = con.cursor()
    return (con, c)

#create table
def create_table():
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

#view the rows
def data_from_database():
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

#insert data into table
def insert_data(company, firstname, lastname, password):
    
    try:
        con, c = open_connection()
        c.execute("INSERT INTO password (Company, Firstname, Lastname, Password) VALUES (?,?,?,?)",(company, firstname, lastname, password))
        con.commit()
        c.close()
        con.close()
        return True
    except:
        c.close()
        con.close()
        return False

def delete_password():
    ...

if __name__ == "__main__":
    ...