from waitress import serve
from api import app

def render():
    serve(app,host="127.0.0.1",port=8001,url_prefix="")