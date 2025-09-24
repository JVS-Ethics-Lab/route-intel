from fastapi import FastAPI

app = FastAPI(title="Route Intel API")

@app.get("/health")
def health_check():
    return {"status": "ok"}
