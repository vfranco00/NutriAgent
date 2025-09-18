from fastapi import FastAPI
from app.routers import auth, foods, preferences

app = FastAPI(title="NutriAgent API", version="0.1.0")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(foods.router, prefix="/foods", tags=["foods"])
app.include_router(preferences.router, prefix="/preferences", tags=["preferences"])

@app.get("/")
def root():
    return {"ok": True, "name": "NutriAgent API"}