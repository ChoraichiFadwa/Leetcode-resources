# 🏛️ Software Architecture

---

## 🔹 Monolithic vs Microservices

### 🧾 Definitions

- **Monolith**: Single-tiered app where all features run together.
- **Microservices**: Modular services that run independently and communicate via APIs.

### ✅ Pros & Cons

| Aspect | Monolith | Microservices |
|--------|----------|----------------|
| Deployment | Simple | Complex |
| Scaling | Hard | Easy (per service) |
| Codebase | One big chunk | Modular |
| Failures | All crash together | Isolated failure |

### 🔍 Real-life Example

- **Monolith**: Early-stage startups (quick to build)
- **Microservices**: Netflix, Amazon (scale & modular)

### ❓ Interview Tip

> “How do you migrate from monolith to microservices?”
- Identify domain boundaries.
- Split service by business capability.
- Introduce API Gateway.

---

## 🔹 API Types (REST vs SOAP vs GraphQL)

| API Type   | Description |
|------------|-------------|
| **REST**   | Resource-based, uses HTTP verbs. Most common. |
| **SOAP**   | XML-based, strict contracts. Used in legacy or enterprise systems. |
| **GraphQL**| Query language for APIs. Ask only what you need. |

### 🎯 REST Best Practices
- Use nouns in URLs: `/users/123`
- Use correct HTTP methods: `GET`, `POST`, `PUT`, `DELETE`
- Use status codes properly (`200`, `404`, `500`...)

---

## 🔹 API Versioning

- `v1`, `v2` in URL path: `/api/v1/users`
- Can also use headers (`Accept: application/vnd.myapp.v1+json`)

---

## 🔹 Interview Sample Qs

> **Q:** What’s the main reason companies move from monoliths to microservices?

**A:** To allow teams to work independently, deploy faster, and scale parts of the system individually.

> **Q:** What are the trade-offs of microservices?

**A:** Complexity in deployment, service discovery, data consistency, and inter-service communication.
---
## 🧪 Practice Tips

- Try building a simple REST API in Flask or FastAPI.
- Use Postman to test your endpoints.
