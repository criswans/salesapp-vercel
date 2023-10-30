from fastapi import FastAPI,Request, Depends, HTTPException
# from flask import Flask, jsonify, request, make_response
import psycopg2
from pydantic import BaseModel
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

class CompanyCreate(BaseModel):
    name: str
    pic_url: str

@app.post("/add_company")
def read_root(company_data: CompanyCreate):
        
    try:
        query = "INSERT INTO company (name, pic_url) VALUES (%s, %s) RETURNING company_id"
        cur.execute(query, (company_data.name, company_data.pic_url))
        company_id = cur.fetchone()[0]
        conn.commit()

        return {
            "status": "SUCCESS",

            "data": {
                "company_id": company_id,
                "name": company_data.name,
                "pic_url": company_data.pic_url
            }
        }
    except Exception as e:
        return {
            "status": "FAILED",
            "error": str(e)
        }
        
class UserCreate(BaseModel):
    email: str
    name: str
    role: str
    pic_url: str
    company_id: int
        
@app.post("/add_user")
def read_root(user_data: UserCreate):
        
    try:
        
        query2 = "SELECT * FROM users WHERE email = %s RETURNING user_id" 
        cur.execute(query2, (user_data.email))
        user = cur.fetchone()[0]
        
        if user:
            return{
                "status" : "FAILED"
            }
        else:
        
        
            if user_data.company_id != 0:     
                query = "INSERT INTO users (email, name, role, pic_url, company_id) VALUES (%s, %s, %s,%s, %s) RETURNING user_id"
                cur.execute(query, (user_data.email, user_data.name, user_data.role, user_data.pic_url, user_data.company_id))
                company_id = user_data.company_id
                user_id = cur.fetchone()[0]
                conn.commit()
            else:
                query1 = "INSERT INTO company (name, pic_url) VALUES (%s, %s) RETURNING company_id"
                cur.execute(query1, ("company name", ""))
                company_id = cur.fetchone()[0]
                query = "INSERT INTO users (email, name, role, pic_url, company_id) VALUES (%s, %s, %s,%s, %s) RETURNING user_id"
                cur.execute(query, (user_data.email, user_data.name, user_data.role, user_data.pic_url, company_id))
                user_id = cur.fetchone()[0]
                conn.commit()
                
                        
            return {
                "status": "SUCCESS",
                "data": {
                    "user_id": user_id,
                    "email" : user_data.email,
                    "name": user_data.name,
                    "role": user_data.role,
                    "pic_url": user_data.pic_url,
                    "company_id" : company_id
                }
            }   
        
    except Exception as e:
        return {
            "status": "FAILED",
            "error": str(e)
        }
   


@app.get('/get_company')
def read_root(company_id: str):    
    try:
        if company_id:
            query = "SELECT * FROM company WHERE company_id = %s"
            cur.execute(query, (company_id,))
            company_data = cur.fetchone()

            if company_data:
                company_json = {
                    "company_id": company_data[0],
                    "name": company_data[1],
                    "pic_url": company_data[2],
                    # Tambahkan kolom lainnya sesuai dengan struktur tabel
                }

                return {
                    "status": "SUCCESS",
                    "data": company_json
                }
            else:
                return {
                    "status": "FAILED",
                    "error": "Company not found"
                }
        else:
            # Jika company_id tidak disertakan, ambil semua data perusahaan
            query = "SELECT * FROM company"
            cur.execute(query)
            company_data = cur.fetchall()

            company_list = []
            for row in company_data:
                company_json = {
                    "company_id": row[0],
                    "name": row[1],
                    "pic_url": row[2],
                    # Tambahkan kolom lainnya sesuai dengan struktur tabel
                }
                company_list.append(company_json)

            return {
                "status": "SUCCESS",
                "data": company_list
            }
    except Exception as e:
        return {
            "status": "FAILED",
            "error": str(e)
        }
        
@app.get('/get_user')
def read_root(user_id: str):
    
    try:
        if user_id:
            query = "SELECT * FROM users WHERE user_id = %s"
        else:
            query = "SELECT * FROM users"
        
        cur.execute(query, (user_id,))
        user_data = cur.fetchone()

        if user_data:
            user_json = {
                "user_id": user_data[0],
                "email" : user_data[1],
                "name": user_data[2],
                "role" : user_data[3],
                "pic_url" : user_data[4],
                "company_id" : user_data[5]
            }
            return {
                "status": "SUCCESS",
                "data": user_json
            }
        else:
            return {
                "status": "FAILED",
                "error": "user not found"
            }
    except Exception as e:
        return {
            "status": "FAILED",
            "error": str(e)
        }


    
