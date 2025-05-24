from fastapi import APIRouter
import translate
import endpoint

router = APIRouter()

router.include_router(translate.router, prefix='/translate', tags=['trabslate'])
router.include_router(endpoint.router, tags=["Home"])