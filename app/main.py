from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(
    title="Cloud Native GitOps App",
    version="1.0.0"
)

Instrumentator().instrument(app).expose(app)


@app.get("/")
def root():
    return {
        "message": "Cloud Native GitOps Platform",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/api/info")
def info():
    return {
        "application": "gitops-app",
        "environment": "development",
        "platform": "Kubernetes"
    }


@app.get("/api/version")
def version():
    return {
        "version": "1.0.0"
    }