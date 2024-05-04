from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.api_route("/", methods=['GET', 'POST'])
def root():
    return {"message":"Hello World"}

@app.api_route("/posts", methods=['GET', 'POST'])
def get_posts():
    return {"date": "This is your posts"}

@app.api_route('/createposts', methods=['GET', 'POST'])
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title {payload['title']} content: {payload['content']}"}