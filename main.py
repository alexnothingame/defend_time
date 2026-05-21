from fastapi import FastAPI
import time

app = FastAPI()
time_requests_count = 0

@app.get("/time")
def get_time():
    global time_requests_count
    time_requests_count += 1
    return {"time": int(time.time())}

@app.get("/metrics")
def get_metrics():
    return {"count": time_requests_count}