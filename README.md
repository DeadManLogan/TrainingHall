# 🐳 PostgreSQL with Docker & VS Code

This guide walks you through setting up **PostgreSQL in Docker**, connecting from **VS Code**, and running **SQL files** for schema and seed data.

---

## 📦 Installation

1. **Install Docker Desktop**
   - [Download here](https://www.docker.com/products/docker-desktop/)
   - Verify install:
     ```bash
     docker --version
     ```

2. **Install VS Code**
   - [Download here](https://code.visualstudio.com/)

3. **Install VS Code Extensions**
   - `Docker` (Microsoft official)

---

## 🛠️ Project Setup

1. Create containers and start them:
   ```bash
   docker compose up -d
2. Enter the PostgreSQL CLI:
    ```bash
   docker exec -it my_postgres psql -U myuser -d mydatabase
