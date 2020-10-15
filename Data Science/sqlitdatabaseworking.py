import pandas as pd
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    ''' create a database connection to a SQlite database'''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    finally:
        if conn:
            conn.close()
if __name__ == "__main__": create_connection("C:/Users/user/Documents/2020-Kalkaal Speciality Hospital/Abdullah/Daily Data/labrequests.db")


