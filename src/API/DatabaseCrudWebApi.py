from InfraStructure.TimeseriesScoreService import TimeseriesScoreService
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from services import UserService  # assuming services.py contains all your service classes

app = FastAPI()

app.mount("/templates", StaticFiles(directory="templates"), name="templates")
templates = Jinja2Templates(directory="templates")

@app.get("/map", response_class=HTMLResponse)
async def map(request: Request):
    return templates.TemplateResponse("map.html", {"request": request})

class User(BaseModel):
    username: str
    password: str

@app.post("/user")
async def create_user(user: User):
    UserService().create_user(user.username, user.password)
    return {"message": "User created successfully"}

@app.get("/user/{user_id}")
async def read_user(user_id: str):
    user = UserService().get_user(user_id)
    if user is None:
        return {"error": "User not found"}
    else:
        return {"username": user.Str_UserName}

@app.put("/user/{user_id}")
async def update_user(user_id: str, user: User):
    UserService().update_user(user_id, user.username, user.password)
    return {"message": "User updated successfully"}

@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    UserService().delete_user(user_id)
    return {"message": "User deleted successfully"}

@app.get("/scores")
async def read_scores():
    # Just an example, replace with your actual method for getting scores
    scores = TimeseriesScoreService().get_all_scores()
    return scores
