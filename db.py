import sqlite3

class Database:
    #constructor of the class Database also called as an initializer in python
    #a constructor runs when the object is instanciated
    #self = this , db = database name
    def __init__(self,db):
        #db is the name of the database
        #connection is the property through which we will be connecting to our database
        self.connection = sqlite3.connect(db)
        #database_cursor is the name of the cursor for database db
        self.database_cursor = self.connection.cursor()
        #now here we are executing our cursor to create a database if not already present
        #the table inside the database db is bill table
        #bill table will be created inside this database db
        self.database_cursor.execute("CREATE TABLE IF NOT EXISTS bill (id INTEGER PRIMARY KEY, current_date_time text,customer_name text, customer_phone_number text,customer_email_address text, bath_soap text, face_cream text, face_wash text, hair_spray text, hair_gel text, body_lotion text, rice text, food_oil text, daal text, wheat text, sugar text, tea text, maza text, coke text, frooti text, thumbs_up text, limca text, sprite text, total_cosmetic_price text, total_grocery_price text, total_cold_drink_price text, cosmetics_tax text, grocery_tax text, cold_drinks_tax text, Total_amount_to_be_payed_by_customer text)")
        #now we will commiting these changes to our database db
        self.connection.commit()

    def fetch(self):
        #here we are reading the bill table from our database db
        # * means we want all the information present inside our bill table of our database db
        self.database_cursor.execute("SELECT * FROM bill")
        #it will get all the rows
        rows = self.database_cursor.fetchall()
        return rows

    def insert(self, current_date_time,customer_name, customer_phone_number, customer_email_address, bath_soap, face_cream, face_wash, hair_spray, hair_gel, body_lotion, rice,food_oil, daal, wheat, sugar, tea, maza, coke, frooti, thumbs_up, limca, sprite, total_cosmetic_price, total_grocery_price, total_cold_drink_price, cosmetics_tax, grocery_tax, cold_drinks_tax, Total_amount_to_be_payed_by_customer):
        #the "INSERT INTO bill VALUES" line will insert the values passed by the user
        #"(NULL, ?, ?, ?, ?)" prevents from sql injection
        # variable python tuple => (customer_name,customer, retailer, price) are the arguments that are passed in to this insert function
        self.database_cursor.execute("INSERT INTO bill VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (current_date_time,customer_name,customer_phone_number,customer_email_address, bath_soap, face_cream, face_wash, hair_spray, hair_gel, body_lotion, rice,food_oil, daal, wheat, sugar, tea, maza, coke, frooti, thumbs_up, limca, sprite, total_cosmetic_price, total_grocery_price, total_cold_drink_price, cosmetics_tax, grocery_tax, cold_drinks_tax, Total_amount_to_be_payed_by_customer))
        #now commit these changes to our database
        self.connection.commit()

    def remove(self,id):
        # "DELETE FROM bill WHERE id=?" is the sql command to delete a record from the table named bill
        # (id,) is a tuple a normal python tuple id is the variable passed in this function remove as an argument
        self.database_cursor.execute("DELETE FROM bill WHERE id=?",(id,))
        self.connection.commit()

    def update(self, id, current_date_time,customer_name, customer_phone_number, customer_email_address, bath_soap, face_cream, face_wash, hair_spray, hair_gel, body_lotion, rice,food_oil, daal, wheat, sugar, tea, maza, coke, frooti, thumbs_up, limca, sprite, total_cosmetic_price, total_grocery_price, total_cold_drink_price, cosmetics_tax, grocery_tax, cold_drinks_tax, Total_amount_to_be_payed_by_customer):
        #"UPDATE bill SET customer_name = ? , customer = ? , retailer = ? , price = ? WHERE id=?" is the sql command that will update the information in our parts column
        #customer_name = ? , customer = ? , retailer = ? , price = ? are the column names of our bill table
        # WHERE id=? is the where clause which will match the id and update the information of the record of matching id
        # (customer_name,customer,retailer,price,id) is a python tuple containing our arguments passed on to this update function
        self.database_cursor.execute("UPDATE bill SET current_date_time = ? , customer_name = ? , customer_phone_number = ? , customer_email_address = ? , bath_soap = ? , face_cream = ? , face_wash = ? , hair_spray = ? , hair_gel = ? , body_lotion = ? , rice,food_oil = ? , daal = ? , wheat = ? , sugar = ? , tea = ? , maza = ? , coke = ? , frooti = ? , thumbs_up = ? , limca = ? , sprite = ? , total_cosmetic_price = ? , total_grocery_price = ? , total_cold_drink_price = ? , cosmetics_tax = ? , grocery_tax = ? , cold_drinks_tax = ? , Total_amount_to_be_payed_by_customer = ? WHERE id=?", (customer_name,customer_phone_number, bath_soap, face_cream, face_wash, hair_spray, hair_gel, body_lotion, rice,food_oil, daal, wheat, sugar, tea, maza, coke, frooti, thumbs_up, limca, sprite, total_cosmetic_price, total_grocery_price, total_cold_drink_price, cosmetics_tax, grocery_tax, cold_drinks_tax, Total_amount_to_be_payed_by_customer,id))
        self.connection.commit()

    # now here we will call the destructor
    #destructor is called when all references of the objects have been deleted
    def __del__(self):
        self.connection.close()