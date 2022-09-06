import os
from waitress import serve
#from .index import app
this_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(this_dir)

# run the server
def run_server(app_):
    serve(app_,host="127.0.0.1",port=8001,url_prefix="")
