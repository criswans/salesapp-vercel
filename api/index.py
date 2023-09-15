from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from model import Task
from schema import task_schema
from session import get_database_session
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Server is up and running!"}

@app.get("/task/{id}", response_model = task_schema, status_code=200)
async def get_task(Name:str,db: Session = Depends(get_database_session)):
   task = db.query(Task).get(Name)
   return task