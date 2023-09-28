from fastapi import FastAPI,Request, Depends, HTTPException
# from flask import Flask, jsonify, request, make_response
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
def read_root(company_id: str):
    
    try:
        if company_id:
            query = "SELECT * FROM company WHERE company_id = %s"
        else:
            query = "SELECT * FROM company"
        
        cur.execute(query, (company_id,))
        company_data = cur.fetchone()

        if company_data:
            # Jika data perusahaan ditemukan, kirimkan sebagai respons
            return {
                "status": "SUCCESS",
                "data": company_data
            }
        else:
            return {
                "status": "FAILED",
                "error": "Company not found"
            }
    except Exception as e:
        return {
            "status": "FAILED",
            "error": str(e)
        }


    
