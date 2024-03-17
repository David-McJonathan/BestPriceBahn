import sqlite3
from sqlite3 import Error



def sendSQLdata(start, ziel, tripDate, checkDate, preis):
    """
    Create a new colum into the table
    :param start:
    :param ziel:
    :param tripDate:
    :param checkDate:
    :param preis:
    """


    print(start + ziel + str(tripDate) + str(checkDate))