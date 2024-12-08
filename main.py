'''Main'''
from fastapi import FastAPI, Path
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse

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

@app.get('/search/{string}')
def searcg(string: str = Path(min_length=2, max_length=40)):
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
