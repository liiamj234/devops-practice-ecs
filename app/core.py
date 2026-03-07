from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {"message": "DevOps Practice App running"}

@router.get("/health")
def health():
    # AWS ALB will check this repeatedly.
    # If this fails, AWS stops routing traffic to your service.
    return {"status": "ok"}