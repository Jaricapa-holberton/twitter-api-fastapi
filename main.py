# Python
# Pydantic
# FastAPI
from fastapi import FastAPI


# Models
from models import User, UserIn, UserOut
from models import Tweet

app = FastAPI()


@app.get(path="/", tags=["Home"])
def home():
    return {"message": "Welcome"}