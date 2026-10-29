
from fastapi import FastAPI
from log_generator import generate_log

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to OpsPilot AI!"}
@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/logs")
def get_logs():
    logs = []

    for _ in range(10):
        logs.append(generate_log())

    return {"logs": logs}
