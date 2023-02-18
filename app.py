from fastapi import FastAPI, Form
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from os.path import sep

app = FastAPI()

users = {
    "testrng@rng.com": {
        "name": "Андрей",
        "password": "1"
    },
    "lenya@gg.com": {
        "name": "Леня",
        "password": "222_test"
    }

}

@app.get("/")
def main_page():
    with open('index.html', encoding='utf-8') as fh:
        main_data = fh.read()
    return Response(content=main_data, media_type='text/html')

@app.post("/welcome-page")
def process_login_page(username: str = Form(...), password: str = Form(...)):
    user = users.get(username)
    if not user or user["password"] != password:
        return Response("че)", media_type='text/html')
    with open(f'welcomepage{sep}hello.html', encoding='utf-8') as fr:
        hello_data = fr.read()
    return Response(content=hello_data, media_type='text/html')

