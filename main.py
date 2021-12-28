# Python
from typing import List , Dict

# Pydantic
# Models
from models import UserBase, User, UserLogin, Tweet

# FastAPI
from fastapi import FastAPI, status, Path

app = FastAPI()

## Auth
@app.post(
    path='/signup',
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary='Register an User',
    tags=['Users']
)
def signup():
    pass

@app.post(
    path='/login',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Login an User',
    tags=['Users']
)
def login():
    pass

## Users

@app.get(
    path='/users',
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary='Show all users',
    tags=['Users']
)
def show_all_users():
    pass

@app.get(
    path='/users/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Show an User',
    tags=['Users']
)
def show_an_user():
    pass

@app.delete(
    path='/users/{user_id}/delete',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Delete an User',
    tags=['Users']
)
def delete_an_user():
    pass

@app.put(
    path='/users/{user_id}/update',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Update an User',
    tags=['Users']
)
def update_an_user():
    pass

## Tweets

### Show  all tweets
@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets",
    tags=["Tweets"]
)
def home():
    # return {"Twitter API": "Working!"}
    pass

### Post a tweet
@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a tweet",
    tags=["Tweets"]
)
def post(): 
    pass

### Show a tweet
@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a tweet",
    tags=["Tweets"]
)
def show_a_tweet(): 
    pass

### Delete a tweet
@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a tweet",
    tags=["Tweets"]
)
def delete_a_tweet(): 
    pass

### Update a tweet
@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweet",
    tags=["Tweets"]
)
def update_a_tweet(): 
    pass