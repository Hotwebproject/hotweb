from waitress import serve
from .api_ import API
from whitenoise import WhiteNoise
import os
def render(app_routes,host="127.0.0.1",port=8001,url_prefix=""):
    # all other app configs to be written here
    curr = os.getcwd()
    static = os.path.join(os.path.dirname(__file__),"router")
    print(f"=======static---->{static}")
    app_ = API(app_routes)
    app_ = WhiteNoise(app_,root=static,prefix="assets/")
    #app_.add_files(static,prefix="/")
    """
    for k,v in app_routes.items():
        if app_routes.routes[k]["static"]:
            # add to whitenoise
            if isinstance(,str):
                
                app_.add_files(app_routes.routes[k]["static"],prefix='') if not app_routes.routes[k]["prefix"] else app_.add_files(app_routes.routes[k]["prefix"],prefix=f'{app_routes.routes[k]["prefix"]}/')
            elif isinstance(,list):
                for static in app_routes.routes[k]["static"]:
                    app_.add_files(app_routes.routes[k]["static"],prefix='') if not app_routes.routes[k]["prefix"] else app_.add_files(app_routes.routes[k]["prefix"],prefix=f'{app_routes.routes[k]["prefix"]}/')
    """
    #print(f"======APP Routes :: {app.routes}")
    try:
        serve(app_,host=host,port=port,url_prefix=url_prefix)
        print("<--------------------Hotweb : Powered by ManlowCharumbira---------------------->")
        print(f"                    APP RUNNING ON --> {host}:{port}")
        print("<--------------------HAPPY BLOGGING-------------------------------------------->")
    except Exception as e:
        print(f"An error occured while trying to serve the app :: {e}")