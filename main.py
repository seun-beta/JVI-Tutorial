from typing import Dict

from fastapi import FastAPI


app = FastAPI()

@app.get(path="/", description="First route", deprecated=False, status_code=200, response_model=Dict[str, str], tags="AAA", summary="A new route")
async def root():
    return {"data": "Hello"}


@app.post("/{id}", tags="AAA")
async def post(id):
    return {"data": "Hello from this route"}
