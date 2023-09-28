from fastapi import FastAPI, Depends, HTTPException
from flask import Flask, jsonify, request, make_response
import psycopg2
conn = psycopg2.connect(database = "verceldb", 
                        user = "default", 
                        host= 'ep-red-grass-55948427-pooler.ap-southeast-1.postgres.vercel-storage.com',
                        password = "io6VkLhbY3pZ",
                        port = 5432)

    
cur = conn.cursor()





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


@app.route('/get_company')
def get_company():
    
    company_id =  request.args.get("company_id")
    return company_id
    
    # try:
    #     dt = Data()
    #     values = ()
    #     if request.method == "GET":
    #         if company_id:
    #             query = "SELECT * FROM company where company_id = %s"
    #             values = (company_id,)
    #         else:
    #             query =  "SELECT * FROM company"

    #     data = dt.get_data(query, values)
             

    # except Exception as e:
    #     return make_response(jsonify({
    #         "status" : "FAILED",
    #         "error" : str(e)}), 400)
    
    # return make_response(jsonify({
    #     "status" : "SUCCESS",
    #     "data" : str(data)}), 200)

