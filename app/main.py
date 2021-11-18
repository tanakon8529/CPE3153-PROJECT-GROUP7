from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"API-CPE3153": "Welcome"}

