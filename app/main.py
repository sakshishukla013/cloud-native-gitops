from fastapi import FastAPI

app = FastAPI(
    title="Cloud Native GitOps App",
    version="1.0.0"
)


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