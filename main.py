'''Main'''
from fastapi import FastAPI, Query, Request, Cookie, Form
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse, Response
from pydantic import BaseModel

# pylint: disable=C0103

app = FastAPI()

@app.get("/")
def read_root():
    '''Root function'''
    html_content = "<h1>Hello World</h1>"
    return HTMLResponse(content=html_content)

@app.get('/greet/{name}')
def name(name1):
    '''Name fuction'''
    content = f'<h1>Hello, {name1}<h1>'
    return HTMLResponse(content=content)

@app.get('/search/')
def searcg(string: str = Query(default='None', min_length=2, max_length=40)):
    '''Search query'''
    html = f'<h2>You searched: {string}<h2>'
    return HTMLResponse(content=html)

@app.get('/json')
def jsonsender():
    '''Json sender function'''
    json = {
        'name': 'Nikita',
        'age': '21',
        'hobbies': 'programming'
    }
    return json

@app.get('/file')
def file_sender():
    '''A file sending function'''
    return FileResponse("Public/text.txt",
                        filename="A_Text_File.txt",
                        media_type="application/octet-stream")

@app.get('/redirect')
def redirection_handler():
    '''a function that will redirect'''
    return RedirectResponse('/', status_code=308)

@app.get('/headers')
def get_headers(request: Request):
    '''Function that retrieves headers from http request'''
    headers = request.headers
    return headers

@app.get('/set-cookie')
def cookie_setter(response: Response):
    '''Sets cookies in the browser'''
    response.set_cookie(key='username', value='your_name')
    return {'message': 'Cookies set'}

@app.get('/get-cookie')
def cookie_getter(username = Cookie()):
    '''Gets cookies in the browser'''
    return {'UserName': username}

@app.get('/login')
def user_login():
    '''Functiont that logs user in'''
    return FileResponse("public/login.html")

@app.post('/login_post')
def log_in(username = Form(), password= Form()):
    '''Processes the HTTP post request'''
    html = f'<h1>Welcome, {username}<h1>'
    return HTMLResponse(content=html)

@app.get('/register')
def user_register():
    '''sends user HTML page'''
    return FileResponse('public/register.html')


class UserData(BaseModel):
    '''Base model for user data'''
    username: str
    password: str
    email: str

usename = 'default'

@app.post('/register_post')
def user_register_post(user: UserData):
    '''Processes the HTTP post request'''
    html = f'<h1>Registered, {user.usename} successfully</h1>'
    return HTMLResponse(content=html)

class UserModel:
    '''Class that defines users'''
    def __init__(self, id, username, password, email):
        self.id: int = id
        self.username: str = username
        self.password: str = password
        self.email: str = email

users = [
    UserModel(0, 'SunPixel', 'Qwerty', '22@33'),
    UserModel(1, '1223', 'Qwerty', '23@34'),
    UserModel(2, 'PixelS', 'Kenek', '22@44.ru')
]

@app.get('/users')
def get_users():
    '''A function returning all users of class as JSON'''
    return [user.__dict__ for user in users]

@app.get('/user/{user_id}')
def get_user(user_id: int):
    '''A function returning a user by id'''
    user = next((user for user in users if user.id == user_id), None)
    if user:
        return user.__dict__
    return {'message': 'User not found'}

@app.post('/add_user')
def add_user(user: UserData):
    '''A function to add a new user using POST request'''
    new_id = len(users)
    new_user = UserModel(new_id, user.username, user.password, user.email)
    users.append(new_user)
    return {'message': f'User {user.username} added successfully'}
