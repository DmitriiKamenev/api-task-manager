from fastapi import APIRouter

health_router = APIRouter(prefix="/health", tags=['Проверка'])

@health_router.get('/')
def health():
    return 'Запусщен'