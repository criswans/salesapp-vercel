from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List
# # from model import Task
# # from schema import task_schema
# # from session import get_database_session
# from sqlalchemy.schema import Column
# from sqlalchemy.types import String, Integer, Text
# # from database import Base

# from pydantic import BaseModel
# from typing import Optional
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker


# model.Base.metadata.create_all(bind=engine)
# def create_get_session():
#    try:
#        db = SessionLocal()
#        yield db
#    finally:
#        db.close()
# SQLALCHEMY_DATABASE_URL = "postgres://default:io6VkLhbY3pZ@ep-red-grass-55948427.ap-southeast-1.postgres.vercel-storage.com:5432/verceldb"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# class task_schema(BaseModel):
#    Name :str
#    Owner :str

#    class Config:
#        orm_mode = True

# class Task(Base):
#     tablename = "pets"	
#     Name = Column(String(20))		
#     Owner = Column(Text())
# conn = psycopg2.connect(database = "verceldb", 
#                         user = "default", 
#                         host= 'ep-red-grass-55948427-pooler.ap-southeast-1.postgres.vercel-storage.com',
#                         password = "io6VkLhbY3pZ",
#                         port = 5432)
# cur = conn.cursor()



app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Server is up and running!"}

# @app.get("/insert")
# def read_root():
#     cur.execute("INSERT INTO pets (Name, Owner) VALUES('hehe','Izzy Weber')")
#     conn.commit()
#     cur.close()
#     conn.close()
#     return {"added : data"}

# @app.get("/task/{id}", response_model = task_schema, status_code=200)
# async def get_task(Name:str,db: Session = Depends(get_database_session)):
#    task = db.query(Task).get(Name)
#    return task