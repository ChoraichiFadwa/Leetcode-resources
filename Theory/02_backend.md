# 🔧 Backend Fundamentals

Everything you need to master backend interviews and be solid on server-side systems. Covers HTTP, databases, caching, sessions, and more.

---

## 🌐 1. HTTP Fundamentals

### ✅ Core Concepts
- **HTTP Methods**: `GET`, `POST`, `PUT`, `DELETE`, `PATCH`
- **Status Codes**:
  - `2xx` – Success (e.g., `200 OK`, `201 Created`)
  - `4xx` – Client errors (e.g., `400 Bad Request`, `404 Not Found`)
  - `5xx` – Server errors (e.g., `500 Internal Server Error`)
- **Headers**: Metadata (auth tokens, content-type)
- **Body**: Request/response payload

---

## 🧠 2. Sessions vs Tokens

| Feature     | Sessions (Cookies)             | Tokens (JWT)                  |
|-------------|-------------------------------|-------------------------------|
| Stored In   | Server memory / DB             | Client-side (usually)         |
| Stateless   | ❌ No                          | ✅ Yes                         |
| Scaling     | Harder (need sticky sessions) | Easier                        |
| Use Case    | Traditional web apps           | SPAs, mobile apps             |

- **Session ID** is stored in a cookie.
- **JWT**: Encoded token with payload and signature. Stored in `localStorage` or `Authorization` header.

---

## 🗄️ 3. Databases: SQL vs NoSQL

### SQL (Relational)
- Structured, tables, schemas
- ACID compliant (atomic, consistent, isolated, durable)
- Examples: MySQL, PostgreSQL, SQL Server

### NoSQL
- Flexible schema
- Types: Document (MongoDB), Key-Value (Redis), Column (Cassandra), Graph (Neo4j)
- Use for fast reads, unstructured data

---

## 🔍 4. Caching

### Why cache?
- Reduce DB/API calls
- Speed up response time

### Tools
- **In-memory**: Redis, Memcached
- **Browser**: HTTP cache headers (`Cache-Control`, `ETag`)

### Strategies
- **Write-through**, **Write-back**
- **Cache-aside**
- **Invalidate on update**

---

## ⚙️ 5. Background Jobs / Async Work

- Use when tasks take too long (email sending, image processing)
- Tools: Celery (Python), Sidekiq (Ruby), Bull (Node.js)
- Queue systems: RabbitMQ, Kafka, Redis

---

## 📡 6. Webhooks vs Polling

| Method   | Description |
|----------|-------------|
| Polling  | Client asks repeatedly (“anything new?”) |
| Webhook  | Server pushes updates when something happens |

---

## 📦 7. File Uploads

- Direct upload to backend vs cloud (S3, Firebase)
- Store metadata in DB (filename, path, size)
- Always validate file type and size

---

## 🔐 8. Authentication & Authorization

### Auth Types
- Basic Auth
- Session-based
- Token-based (JWT)
- OAuth2 (login with Google, etc.)

### Common Patterns
- Role-based access control (RBAC)
- Middleware for protected routes

---

## 🔄 9. Pagination

- Use for large datasets
- Types:
  - **Offset**: `?page=2&limit=10`
  - **Cursor-based**: based on last record ID

---

## 🎯 Interview Questions to Practice

- Explain how a REST API handles authentication.
- How would you store user sessions at scale?
- Describe how caching can help optimize a backend.
- When would you use NoSQL over SQL?
- How do background jobs improve app performance?

---

## 🧪 Practice Ideas

- Build a mini-blog API with:
  - CRUD endpoints
  - JWT login system
  - Pagination on posts
  - Redis caching for top posts

---

## 🚧 Tools to Learn

- **Postman** – Test APIs
- **FastAPI / Express / Django** – Backend frameworks
- **Docker** – Run everything in containers
- **Swagger/OpenAPI** – API documentation
