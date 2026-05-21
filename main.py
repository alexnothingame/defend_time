from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/time")
def get_time():
    return {"time": int(time.time())}