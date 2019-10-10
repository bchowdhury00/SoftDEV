#Biraj Chowdhury 
#SoftDev Pd 9
#K17 -- No Trouble : DataBases : SQLITE3 BASICS
#2019 October 09

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

csvFile = ""
DB_FILE="discobandit.db"
db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

def fillDB():
    global csvFile
    #takes in name of csv file and suggested name of table from user
    csvFile = input("Enter Your CSV file: ")
    tableName = input("Enter the name of the table for this file: ")
    #creates string to hold command to create a table
    createTable  = "CREATE TABLE " + tableName + " ("
    with open(csvFile,'r') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = []
        #for loop to access the fieldnames and fill createTable var
        for row in reader:   
            fieldnames = list(row.keys())
            for val in fieldnames:
                type = ""
                if (row.get(val).isnumeric()): #check type of field
                    type = " NUMERIC"
                else:
                    type = " TEXT"
                 #checks if this val is the last field
                if (val != fieldnames[len(fieldnames) - 1]):
                    createTable += (val + type + ",")
                
                else:
                    createTable += (val + type + ");")
            break
        #creates table
        c.execute(createTable)
        #create insertion command for each record
        for row in reader:
            insert = "INSERT INTO " + tableName + " VALUES("
            for val in fieldnames:
                #checks if val is the last field
                if (val != fieldnames[len(fieldnames) - 1]):
                #checks if entry is numeric to see whether or not to add quotes
                    if (row.get(val).isnumeric()):
                        insert += (row.get(val) + ",")
                    else:
                        insert += ("\"" + row.get(val) + "\""+ ",")
                else:
                    #completes string for insertion command
                    insert += (row.get(val) + ");")
                    #executes insertion command
                    c.execute(insert)               
    return
fillDB()
db.commit() #save changes
db.close()  #close database
