import mysql.connector

def conn(user = "root", password = "", host = "localhost", database = "skripsi"):
    conn = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )
    return conn


def select(query, values, conn):
    myCursor = conn.cursor()
    myCursor.execute(query, values)
    row_headers = [x[0] for x in myCursor.description]
    myResult = myCursor.fetchall()
    json_data = []

    for result in myResult:
        json_data.append(dict(zip(row_headers, result)))
    return json_data


def insert(query, val, conn):
    myCursor = conn.cursor()
    myCursor.execute(query, val)
    conn.commit()