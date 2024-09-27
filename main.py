from fastapi import FastAPI , HTTPException
from pydantic import BaseModel,EmailStr,constr
from typing import List, Optional
from datetime import datetime
import logging

app = FastAPI()

class Task(BaseModel):
    task_id: constr(min_length=1)
    description: Optional[str] = None
    completed: bool

class IncomingData(BaseModel):
    user_id: constr(min_length=1)
    email: EmailStr
    timestamp: datetime
    tasks: List[Task]

@app.post("/submit")
async def submit_data(data: IncomingData):
    return {"message": "Data is valid!"}

@app.exception_handler(Exception)
async def validation_exception_handler(request, exc):
    logging.error(f"Validation Error: {exc}")
    raise HTTPException(status_code=422, detail=str(exc))
