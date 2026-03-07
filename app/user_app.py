from fastapi import APIRouter

router = APIRouter()

# ============================================================
# YOUR TUTORIAL CODE GOES IN THIS FILE.
# ============================================================
# Anything in this router becomes available under /app/*
# because main.py mounts it with prefix="/app".
#
# Examples (once you add routes):
#   GET /app/portfolio
#   GET /app/items
#   GET /app/users
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

# Example tutorial pattern:
# @router.get("/items")
# def list_items():
#     return [{"id": 1, "name": "Example"}]