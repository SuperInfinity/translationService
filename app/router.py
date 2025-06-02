from fastapi import APIRouter
import app.translate as translate
import app.endpoint as endpoint

router = APIRouter()

router.include_router(translate.router, prefix='/translate', tags=['trabslate'])
router.include_router(endpoint.router, tags=["Home"])