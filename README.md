# Prisma Test Project

This is a sample project demonstrating the use of FastAPI with Prisma.

## Local Development

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv)
- Docker

### 1. Clone the repository

```bash
git clone <repository-url>
cd prisma-test
```

### 2. Set up environment variables

Create a `.env` file by copying the sample:

```bash
cp .env-sample .env
```

Update the `.env` file with your database credentials if they differ from the defaults in `docker-compose.yaml`.

### 3. Start the database

```bash
docker-compose up -d
```

### 4. Install dependencies

```bash
uv sync
```

### 5. Run database migrations

```bash
uv run prisma migrate dev
```

### 6. Run the application

```bash
uv run uvicorn main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## Docker

The `docker-compose.yaml` file is provided to run the PostgreSQL database. To start the service, run:

```bash
docker-compose up -d
```

To stop the service:

```bash
docker-compose down
```
