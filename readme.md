# Claim Processing API Documentation

## Introduction:

The Claim Processing API is a backend system developed using FastAPI for handling healthcare claim submissions, updates, and status tracking. This API provides secure endpoints with API Key authentication and is fully containerized using Docker. It also includes CI/CD automation and monitoring suggestions for production environments.

This documentation will guide you through setting up, running, and understanding the structure of the Claim Processing API.

---

## 1. Prerequisites:
- Python 3.8+ installed
- Docker and Docker Compose installed
- Basic understanding of REST APIs
- Internet connection for installing dependencies

---

## 2. Installation:

### a. Clone the Repository
- git clone https://github.com/shrey046/claim-processing-api.git
- cd claim-processing-api

### b. Create Virtual Environment (Optional)
- python3 -m venv venv
- source venv/bin/activate

### c. Install Dependencies
- pip install -r requirements.txt

## 3. Configuration:

- Update any credentials or tokens in .env file if needed (if implemented).
- By default, the project uses SQLite (no setup required). For production, you can switch to PostgreSQL by updating db_config.py and docker-compose.yaml.

## 4. Running the Project:

### a. Using Docker
- docker-compose up --build

### b. Without Docker (Development Mode)
- uvicorn main:app --reload

## 5. API Endpoints:

Method	                    Endpoint	                Description	Auth Required
POST	                    /claims	                    Create a new claim	✅
GET	/claims/{id}	        Retrieve a claim by ID	    ✅
GET	/claims	                Get all claims	            ✅
GET	/claims/status/{id}	    Get status of a claim	    ✅
PUT	/claims/status/{id}	    Update claim status	        ✅
DELETE	/claims/{id}	    Delete a claim	            ✅

## 6. CI/CD Pipeline:
- A CI workflow is configured using GitHub Actions at:
    .github/workflows/ci.yml

It performs:
- Dependency installation
- Code formatting/linting
- Auto testing (if implemented)
- Can be extended to deploy on cloud platforms

## 7. Monitoring & Logging:
Logging:
- Logging is configured using Python's logging module.
- It logs important API and error messages to the console (or file if extended).

Suggested Tools for Monitoring:
- Prometheus + Grafana: For metrics and dashboards
- Sentry: For real-time error monitoring
- ELK Stack: For logs and search

## 8. Known Limitations:
- No persistent database in Docker mode unless configured with a volume.
- No email or webhook notifications on claim updates.

## 9. Future Improvements:
- Add database migrations via Alembic
- Improve monitoring integration with Prometheus
- Add unit and integration test coverage
- Implement admin dashboard for claims