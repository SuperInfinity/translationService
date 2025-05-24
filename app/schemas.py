from pydantic import BaseModel

class TranslationRequet(BaseModel):
    text: str
    languages: list[str]

class TaskResponse(BaseModel):
    task_id: int

class TaskStatus(BaseModel):
    task_id: int
    status: str
    translations: dict[str, str] = {}