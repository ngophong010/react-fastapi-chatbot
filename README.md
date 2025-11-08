# Production-Ready AI Chatbot

A full-stack AI chatbot application built with React, FastAPI, PostgreSQL, and Redis.

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Node.js 18+ (for local development)
- Python 3.11+ (for local development)

### Production Deployment
```bash
# Clone and setup
git clone <repository>
cd react-fastapi-chatbot
cp .env.example .env

# Start all services
make docker-up

# View logs
make docker-logs
```

### Local Development
```bash
# Install dependencies
make install

# Start development environment
make dev
```

## 🏗️ Architecture

- **Frontend**: React 18 + TypeScript + Styled Components
- **Backend**: FastAPI + WebSockets + SQLAlchemy
- **Database**: PostgreSQL + Redis
- **Infrastructure**: Docker + Docker Compose
- **CI/CD**: GitHub Actions

## 📁 Project Structure

```
├── client/                 # React frontend
│   ├── src/
│   ├── Dockerfile
│   └── package.json
├── server/                 # FastAPI backend
│   ├── src/
│   ├── alembic/           # Database migrations
│   ├── tests/
│   ├── Dockerfile
│   └── requirements.txt
├── worker/                # AI processing worker
│   ├── src/
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml     # Multi-service orchestration
├── Makefile              # Development commands
└── .github/workflows/    # CI/CD pipeline
```

## 🛠️ Available Commands

```bash
make help          # Show all commands
make install       # Install dependencies
make dev           # Start development
make test          # Run tests
make lint          # Run linting
make format        # Format code
make docker-up     # Start with Docker
make docker-down   # Stop Docker services
make clean         # Clean up
```

## 🔧 Configuration

Copy `.env.example` to `.env` and configure:

- `DATABASE_URL`: PostgreSQL connection
- `REDIS_URL`: Redis connection
- `HUGGINGFACE_TOKEN`: AI model access
- `JWT_SECRET_KEY`: Authentication secret

## 🧪 Testing

```bash
# Run all tests
make test

# Backend tests only
cd server && python -m pytest tests/ -v

# Frontend tests only
cd client && npm test
```

## 📦 Deployment

### Docker Production
```bash
docker-compose -f docker-compose.prod.yml up -d
```

### Manual Deployment
1. Build frontend: `cd client && npm run build`
2. Setup database: `cd server && alembic upgrade head`
3. Start services: `uvicorn main:api --host 0.0.0.0 --port 8000`

## 🔍 Monitoring

- Health check: `GET /test`
- Metrics: Available via FastAPI `/metrics`
- Logs: `docker-compose logs -f`

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/name`
3. Run tests: `make test`
4. Submit pull request

## 📄 License

MIT License - see LICENSE file for details.