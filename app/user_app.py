from fastapi import APIRouter

router = APIRouter()

# ============================================================
# PUT YOUR PYTHON TUTORIAL / APP ROUTES BELOW THIS LINE
# ============================================================
# Anything in this router becomes available under /app/*
# because main.py mounts it with prefix="/app".
#
# Examples:
#   GET /app/portfolio
#   GET /app/version
#   GET /app/items
#
# IMPORTANT:
# - Do NOT define /health here.
# - Keep /health in core.py only.
# ============================================================

@router.get("/portfolio")
def portfolio_placeholder():
    # Replace this later with your portfolio tutorial logic.
    return {
        "name": "Liam",
        "title": "Portfolio Placeholder",
        "projects": [
            {"name": "DevOps Practice ECS", "status": "in progress"}
        ]
    }

@router.get("/version")
def version():
    # This endpoint is for deployment verification.
    # Change the string when you do new reps.
    return {"version": "ops-rep-01"}

# Example tutorial pattern:
# @router.get("/items")
# def list_items():
#     return [{"id": 1, "name": "Example"}]