# ⚡ FastAPI Crash Guide

FastAPI is a modern, async-ready, Python web framework for building APIs quickly and with automatic documentation. It’s known for speed, type-safety, and simplicity.

---

## 🚀 Why FastAPI?
FastAPI is standards-based. It's based on (and fully compatible with) the open standards for APIs: OpenAPI and JSON Schema. The FastAPI website, shown on the slide, provides more information about the framework's features.

1 https://fastapi.tiangolo.com/

✅ Asynchronous by default  
✅ Auto-generates Swagger docs  
✅ Strong typing with Pydantic  
✅ Extremely fast performance (based on Starlette + Uvicorn)

---

## FastAPI vs other python frameworks 
Django has a built-in Object-Relational Mapping or ORM for short. An ORM is software that represents database models as Python objects. FastAPI and Flask do not have a built-in ORM. FastAPI's key difference is that it's designed for APIs without database operations, which can hurt API performance. This makes FastAPI a great framework for high-throughput data and machine learning transactions.
FastAPI and Falsk don't force database so you can choose (SQLAlchemy, Tortoise ORM, Pony ORM, or even raw SQL).
FastAPI is built in ASGI not WSGI like Django and Flask.
Django ORM is great for relational DBs (Postgres, MySQL, SQLite).

But if you want to mix SQL + NoSQL (e.g., MongoDB, Redis), Django’s ORM is not the right tool.
Django ORM = slower for high-concurrency async APIs.
## 🧪 Installation

```bash
pip install fastapi uvicorn
```
Run server for dev (hot reload + debug):
```bash
fastapi dev main.py
```

Run server for prod (no auto reload):

```bash
python main.py
```

if we want to use this, we need in our main.py: 
```bash
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
```

## GET Operations 
designed to retrive information. parameters should only be sent via URL query string.

https://host:portPathQuerystring
example:
https://google.com:80/search?q=fastapi
his tells the handler that we are sending a query parameter named "q" with a value of "fastapi."

# Basic Example of a GET request
```bash
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
```
query parameters
the default value is Fadwa but if we write [name='fast'](https://localhost:8000/hello?name=fast), we will have in the output 
Hello, fast!

```bash
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def read_root(name : str= "Fadwa"): 
    return {"message": "Hello, {name}!"}
```

## POST Operations
the point is to create an object.
parameters can be sent via request body
The header : tells the app how to decode the data correctly => 

## cURL 
CURL refers to client url, it's used for testing purposes.
It's a command line tool to send http requests 
Perfect — let’s break your cURL command **argument by argument** and then I’ll give you the most commonly used options.

---

## 🔹 Your example

```bash
curl \
  -H 'Content-Type: application/json' \
  http://localhost:8000?name=Steve
```

### 1️⃣ `curl`

* This is the **command itself**: start a cURL request.

### 2️⃣ `-H 'Content-Type: application/json'`

* `-H` stands for **Header**.
* HTTP headers provide metadata about the request.
* Here, you tell the server: “I am sending JSON data (even if it’s just a GET request).”

### 3️⃣ `http://localhost:8000?name=Steve`

* The **URL** you’re requesting.
* The `?name=Steve` is a **query parameter** — equivalent to `request.query_params` in FastAPI.

---

## 🔹 Most common cURL arguments

| Argument               | Meaning                                                    |
| ---------------------- | ---------------------------------------------------------- |
| `-X METHOD`            | Specify HTTP method (`GET`, `POST`, `PUT`, `DELETE`, etc.) |
| `-H "Header: value"`   | Add HTTP headers (like Content-Type, Authorization, etc.)  |
| `-d '{"key":"value"}'` | Send data (for POST/PUT requests)                          |
| `-i`                   | Include HTTP response headers in output                    |
| `-v`                   | Verbose mode (prints request/response info)                |
| `-u username:password` | Basic auth credentials                                     |
| `-b "cookie=value"`    | Send cookies                                               |
| `-c cookies.txt`       | Save cookies to a file                                     |
| `-L`                   | Follow redirects if the server responds with a redirect    |
| `--compressed`         | Ask the server to compress the response                    |
| `--header`             | Same as `-H` (long form)                                   |
| `--request`            | Same as `-X` (long form)                                   |
| `--data-urlencode`     | Encode data before sending (useful for query parameters)   |
| `-o filename`          | Save response to a file                                    |

---

### 🔹 Example: POST JSON with cURL

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"name":"Steve", "age":30}' \
  http://localhost:8000/users/
```

* `-X POST` → use POST method
* `-H "Content-Type: application/json"` → tell server we’re sending JSON
* `-d '{...}'` → the data payload

---

✅ **Summary**

* cURL arguments let you control **method, headers, data, auth, verbosity, cookies**, etc.
* You can mix them to test **any kind of FastAPI endpoint** without a browser.

---

If you want, I can make a **complete cheat sheet of every commonly used cURL option specifically for FastAPI testing**, with examples for GET, POST, query parameters, headers, and JSON body.

Do you want me to do that?
the \ means i ll continue in th enext line 


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