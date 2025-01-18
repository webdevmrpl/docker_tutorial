from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session
from models import Task, SessionLocal

app = FastAPI()

class TaskCreate(BaseModel):
    title: str

@app.get("/tasks")
def list_tasks():
    db: Session = SessionLocal()
    tasks = db.query(Task).all()
    db.close()
    return [{"id": t.id, "title": t.title} for t in tasks]

@app.post("/tasks")
def create_task(task_create: TaskCreate):
    db: Session = SessionLocal()
    new_task = Task(title=task_create.title)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    db.close()
    return {"id": new_task.id, "title": new_task.title}