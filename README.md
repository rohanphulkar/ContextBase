# ContextBase

A modern RAG (Retrieval-Augmented Generation) chat application with document management, built with FastAPI and React.

## 🚀 Features

- **Document Management** - Upload and manage documents for RAG processing
- **AI-Powered Chat** - Contextual conversations using OpenAI and vector search
- **Vector Search** - Semantic search powered by Qdrant
- **Monitoring** - Prometheus metrics and cAdvisor for container monitoring
- **Production Ready** - Docker Compose deployment with Nginx reverse proxy

## 🛠️ Tech Stack

| Component            | Technology             |
| -------------------- | ---------------------- |
| **Backend**          | FastAPI, Python 3.12   |
| **Frontend**         | React, Vite            |
| **Database**         | MySQL 8                |
| **Vector Store**     | Qdrant                 |
| **Reverse Proxy**    | Nginx                  |
| **Monitoring**       | Prometheus, cAdvisor   |
| **Containerization** | Docker, Docker Compose |

## 📁 Project Structure

```
ContextBase/
├── client/                 # React frontend
│   ├── src/
│   ├── nginx/             # Nginx configuration
│   └── Dockerfile
├── server/                 # FastAPI backend
│   ├── contextbase/
│   └── Dockerfile
├── prometheus/             # Prometheus configuration
│   └── prometheus.yml
├── docker-compose.yml
├── DEPLOYMENT.md          # Deployment guide
└── README.md
```

## ⚡ Quick Start

### Prerequisites

- Docker and Docker Compose
- OpenAI API Key

### Local Development

1. **Clone the repository**

   ```bash
   git clone https://github.com/rohanphulkar/ContextBase.git
   cd ContextBase
   ```

2. **Configure environment variables**

   ```bash
   cp server/.env.example server/.env
   # Edit server/.env with your configuration
   ```

3. **Start the application**

   ```bash
   docker compose up -d
   ```

4. **Access the application**
   - Frontend: http://localhost
   - API Docs: http://localhost/api/docs
   - Prometheus: http://localhost:9090

## 🔧 Environment Variables

Create a `.env` file in the `server/` directory:

| Variable         | Description         | Required |
| ---------------- | ------------------- | -------- |
| `MYSQL_HOST`     | MySQL host          | Yes      |
| `MYSQL_PORT`     | MySQL port          | Yes      |
| `MYSQL_USER`     | MySQL username      | Yes      |
| `MYSQL_PASSWORD` | MySQL password      | Yes      |
| `MYSQL_DATABASE` | MySQL database name | Yes      |
| `SECRET_KEY`     | JWT secret key      | Yes      |
| `OPENAI_API_KEY` | OpenAI API key      | Yes      |
| `QDRANT_URL`     | Qdrant URL          | Yes      |

For Docker deployment, also set in root `.env`:

| Variable              | Description         |
| --------------------- | ------------------- |
| `MYSQL_ROOT_PASSWORD` | MySQL root password |
| `MYSQL_DATABASE`      | Database name       |

## 🐳 Docker Services

| Service      | Port            | Description             |
| ------------ | --------------- | ----------------------- |
| `client`     | 80              | Nginx serving React app |
| `server`     | 8000 (internal) | FastAPI backend         |
| `mysql`      | 3306 (internal) | MySQL database          |
| `qdrant`     | 6333 (internal) | Vector database         |
| `prometheus` | 9090            | Metrics collection      |
| `cadvisor`   | 8080            | Container monitoring    |

## 📊 Monitoring

- **Prometheus**: http://localhost:9090
- **cAdvisor**: http://localhost:8080

## 🚢 Deployment

See [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed VPS deployment instructions with GitHub Actions.

## 📝 API Documentation

Once running, access the API documentation at:

- **Swagger UI**: http://localhost/api/docs
- **ReDoc**: http://localhost/api/redoc

## 📄 License

MIT License
