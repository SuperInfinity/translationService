from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from pydantic import BaseModel
from starlette.responses import Response
from http import HTTPStatus
import app.schemas as schemas
import app.crud as crud
import app.models as models
from app.database import get_db, engine
from sqlalchemy.orm import Session
from app.utils import perform_translation


models.Base.metadata.create_all(bind=engine)
router = APIRouter()

@router.post("/", response_model=schemas.TaskResponse)
async def translate(request: schemas.TranslationRequet, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    task = crud.create_translation_task(db, request.text, request.languages)
    background_tasks.add_task(perform_translation, task.id, request.text, request.languages,db)

    return {"task_id": task.id}

@router.get("/{task_id}", response_model=schemas.TaskStatus)
def get_translation(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_translation_task(db, task_id)
    if not task:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Task not found")
    return {"task_id": task.id, "status": task.status, "translations": task.translations}