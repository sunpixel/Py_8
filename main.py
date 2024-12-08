'''Main'''
from fastapi import FastAPI, Path
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def read_root():
    '''Root function'''
    html_content = "<h1>Hello World</h1>"
    return HTMLResponse(content=html_content)

@app.get('/greet/{name}')
def name(name):
    '''Name fuction'''
    content = f'<h1>Hello, {name}<h1>'
    return HTMLResponse(content=content)

@app.get('/search/{string}')
def searcg(string: str = Path(min_length=2, max_length=40)):
    '''Search query'''
    html = f'<h2>You searched: {string}<h2>'
    return HTMLResponse(content=html)
