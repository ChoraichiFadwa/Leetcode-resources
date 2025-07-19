# ⚡ FastAPI Crash Guide

FastAPI is a modern, async-ready, Python web framework for building APIs quickly and with automatic documentation. It’s known for speed, type-safety, and simplicity.

---

## 🚀 Why FastAPI?

✅ Asynchronous by default  
✅ Auto-generates Swagger docs  
✅ Strong typing with Pydantic  
✅ Extremely fast performance (based on Starlette + Uvicorn)

---

## 🧪 Installation

```bash
pip install fastapi uvicorn
```
Run server:
```bash
uvicorn main:app --reload
```
## 📄 Basic Example
```bash
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
```

## 📦 Path & Query Parameters
```bash
@app.get("/items/{item_id}")
def get_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
item_id: path param

q: optional query param (?q=test)
```
## 💌 Request Body (with Pydantic)
```bash
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str

@app.post("/users/")
def create_user(user: User):
    return {"msg": f"User {user.name} created!"}
🔐 Dependency Injection (Auth Example)
```
```bash
from fastapi import Depends

def get_token(token: str = ""):
    if token != "secret":
        raise HTTPException(status_code=401)
    return True

@app.get("/secure/", dependencies=[Depends(get_token)])
def secure_endpoint():
    return {"status": "Authorized"}
```
## 🧱 Middleware Example
```bash
from fastapi import Request

@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    return response
```

## 🎛 Background Tasks
```bash
from fastapi import BackgroundTasks

def write_log(msg: str):
    with open("log.txt", "a") as f:
        f.write(msg)

@app.post("/log/")
def log_message(background_tasks: BackgroundTasks, msg: str):
    background_tasks.add_task(write_log, msg)
    return {"status": "Scheduled"}
```
## ✅ Automatic Swagger Docs
FastAPI auto-generates:

/docs (Swagger UI)

/redoc (Redoc UI)

python
Copy
Edit
app = FastAPI(
    title="My API",
    description="An API with docs generated automatically!",
    version="1.0.0"
)
🗃️ Connecting to a Database (SQLAlchemy)
bash
Copy
Edit
pip install sqlalchemy
Example:

python
Copy
Edit
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

Base.metadata.create_all(bind=engine)
🔐 JWT Auth (Simplified Flow)
User logs in with credentials

Backend verifies and returns JWT

Protected routes require token in Authorization: Bearer <token>

Libraries:

bash
Copy
Edit
pip install python-jose passlib[bcrypt]
🧪 Testing FastAPI
bash
Copy
Edit
pip install pytest httpx
python
Copy
Edit
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}
📦 Add-ons You Should Know
Feature	Tool
ORM	SQLAlchemy, SQLModel, Tortoise ORM
Auth	fastapi.security, OAuth2
Background Jobs	BackgroundTasks, Celery
Docs	Built-in Swagger/OpenAPI
Async Web Server	Uvicorn (or Hypercorn)

💡 Project Ideas
Todo API – CRUD operations, SQLite DB

Blog API – JWT auth, users + posts, pagination

Email sender – Background tasks + Celery + Redis

File uploader – Validate type/size, save to disk or S3

👑 Final Notes
Keep your main.py clean; split into routers/modules as project grows

Always use type hints (FastAPI depends on them!)

Use .env files for secrets/config

Leverage Depends() to inject logic anywhere (auth, DB, logging, etc.)

✨ You're ready to build badass APIs — modern, fast, and scalable!
yaml
Copy
Edit

---

## ✅ What’s Next?

- Add file: `theory/fastapi_crash_guide.md`
- Commit message:  
  `feat(theory): add FastAPI crash guide with examples and best practices`

---

Let me know if you want:
- A **mini-project scaffold** (todo app or blog)
- A **Dockerized FastAPI setup**
- Or continue with `03_ml_ai.md`

You're building a repo that’ll outlive interview seasons — it’s a whole portfolio now 💥