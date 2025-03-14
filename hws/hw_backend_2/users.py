from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    username: str

users = [
    User(id=1, email='bbbauka@gmail.com', first_name='Bauyrzhan', last_name='Kazbekov', username='BillMurray45'),
    User(id=2, email='assseeelya@gmail.com', first_name='Assel', last_name='Yeskuatova', username='Asselya'),
    User(id=3, email='rusik@gmail.com', first_name='Ruslan', last_name='Kazbekov', username='Rusikkkk'),
    User(id=4, email='beka@gmail.com', first_name='Berik', last_name='Kazbekov', username='Bekaaa'),
    User(id=5, email='aidana@gmail.com', first_name='Aidana', last_name='Bekturganova', username='aidook'),
    User(id=6, email='aizzz@gmail.com', first_name='Aizat', last_name='Unerkhanov', username='aizz777')
]

@app.get("/users/", response_class="HTMLResponse")
async def get_users(request: Request, page: int = 1, limit: int = 2):
    start = (page - 1) * limit
    end = start + limit
    paginated_users = users[start:end]

    return templates.TemplateResponse("index.html", {
        "request": request,
        "users": paginated_users,
        "page": page,
        "limit": limit
    })


@app.get("/users/{id}", response_class="HTMLResponse")
async def get_user_by_id(request: Request, id: int):
    user = next((user for user in users if user.id == id), None)

    if not user:
        raise HTTPException(status_code=404, detail="User not found!")

    return templates.TemplateResponse("find_id.html", {
        "request": request,
        "user": user
    })