from fastapi import FastAPI

@app.get("/")
def read_root():
    return {"API": "Molog_WMS"}

