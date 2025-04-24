from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, nfactorial!"}


@app.get("/{num}")
def num_fact(num: int):
    return {"factorial": math.factorial(num)}


@app.post("/meaning-of-life")
def meaning_of_life():
    return {"meaning": "42"}
