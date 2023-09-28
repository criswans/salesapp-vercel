from fastapi import FastAPI, Depends, HTTPException
from flask import Flask, jsonify, request, make_response
import psycopg2
conn = psycopg2.connect(database = "verceldb", 
                        user = "default", 
                        host= 'ep-red-grass-55948427-pooler.ap-southeast-1.postgres.vercel-storage.com',
                        password = "io6VkLhbY3pZ",
                        port = 5432)
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
    
cur = conn.cursor()

class Data:
    def __init__(self):
        self.mydb = conn()

    def get_data (self, query, values):
        return select(query, values, self.mydb)
    
    def insert_data (self, query, val):
        return insert(query, val, self.mydb)



app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Server is up and running!"}

@app.get("/insert")
def read_root():
    cur.execute("INSERT INTO pets (Name, Owner) VALUES('hehe','Izzy Weber')")
    conn.commit()
    cur.close()
    conn.close()
    return {"added : data"}

@app.route('/get_company', methods=['GET'])
def get_company():
    
    company_id =  request.args.get("company_id")
    
    try:
        dt = Data()
        values = ()
        if request.method == "GET":
            if company_id:
                query = "SELECT * FROM company where company_id = %s"
                values = (company_id,)
            else:
                query =  "SELECT * FROM company"

        data = dt.get_data(query, values)
             

    except Exception as e:
        return make_response(jsonify({
            "status" : "FAILED",
            "error" : str(e)}), 400)
    
    return make_response(jsonify({
        "status" : "SUCCESS",
        "data" : str(data)}), 200)

