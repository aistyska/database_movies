import sqlite3

def open_connection():
    db_host = "movies.db"
    connection = sqlite3.connect(db_host)
    cursor = connection.cursor()
    return connection, cursor

def close_connection(connection):
    connection.close()


def no_return_query(query):
    try:
        connection, cursor = open_connection()
        cursor.execute(query)
        connection.commit()
    except sqlite3.DataError as error:
        print(error)
    finally:
        close_connection(connection)


def insert_query(query, p):
    try:
        connection, cursor = open_connection()
        cursor.execute(query, p)
        connection.commit()
        return cursor.lastrowid
    except sqlite3.DataError as error:
        print(error)
    finally:
        close_connection(connection)
    return None


def select_query(query, p = None):
    try:
        connection, cursor = open_connection()
        if p == None:
            cursor.execute(query)
        else:
            cursor.execute(query, p)
        return cursor.fetchall()
    except sqlite3.DataError as error:
        print(error)
    finally:
        close_connection(connection)
    return None


