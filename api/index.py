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


@app.post("/insert")
def read_root():
    
    try:
        cur.execute("INSERT INTO company (name) VALUES('hehe')")
        conn.commit()
        cur.close()
        conn.close()
        return {"added : data"}
        
    except Exception as e:
        
        return e
   


@app.get('/get_company')
def read_root():
    company_id =  request("company_id")
    return make_response(jsonify({
        "status" : "SUCCESS",
        "data" : str(company_id)}))
    

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

