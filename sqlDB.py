import sqlite3
from sqlite3 import Error


def createConnection(db_file):

    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return connection


def createDatabase(connection):

    sqlCreateTable = """ CREATE TABLE IF NOT EXISTS strecke (
                                        id integer PRIMARY KEY,
                                        start text NOT NULL,
                                        ziel text NOT NULL
                                        tripDate text NOT NULL,
                                        checkDate text NOT NULL,
                                        preis_1 integer NOT NULL,
                                        preis_2 integer NOT NULL,
                                        preis_3 integer NOT NULL,
                                        preis_4 integer NOT NULL,
                                        preis_5 integer NOT NULL,
                                    ); """

    
    if connection is not None:
        try:
            c = connection.cursor()
            c.execute(sqlCreateTable)

        except Error as e:        
            print(e)

    else:
        print("Error! connection is None")




def startSQLdb():

    database = "database-BahnPreis.db"

    connection = createConnection(database)

    createDatabase(connection)

    return connection




def sendSQLdata(connection, data):
    """
    Create a new colum into the table
    :param depature: as String
    :param destination: as String
    :param tripDate: as String
    :param checkDate: as String
    :param preis: as int array
    """

    sql = ''' INSERT INTO strecke(depature,destination,tripDate,checkDate,preis_1,preis_2,preis_3,preis_4,preis_5)
              VALUES(?,?,?,?,?,?,?,?,?) '''
    
    cur = connection.cursor()
    cur.execute(sql, data)
    connection.commit()
    return cur.lastrowid




    print(depature + destination + str(tripDate) + str(checkDate))