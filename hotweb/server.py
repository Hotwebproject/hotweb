from waitress import serve
from api.api import API
from whitenoise import WhiteNoise
import os
def render(app_routes,host="127.0.0.1",port=8001,url_prefix=""):
    # all other app configs to be written here
    curr = os.getcwd()
    static = os.path.join(curr,"router")
    app_ = API(app_routes)
    app_ = WhiteNoise(app_,root=static)
    app_.add_files(static,prefix="/")
    """
    app_.add_files(path,prefix='')
    """
    #print(f"======APP Routes :: {app.routes}")
    serve(app_,host=host,port=port,url_prefix=url_prefix)