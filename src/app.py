from fastapi import FastAPI, HTTPException
from src.functional import calculate

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/calculate/{num1}/{num2}")
async def calculate_endpoint(num1: int, num2: int):
    try:
        result = calculate(num1, num2)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))