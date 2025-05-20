

from fastapi import FastAPI, Query

app = FastAPI()

@app.post("/trip/invoke")
def invoke_trip(input: str = Query(...)):
    return {"message": "Trip planning received", "input": input}
