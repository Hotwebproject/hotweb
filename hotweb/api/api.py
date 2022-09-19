from webob import Response,Request
import time
#from routes import Router
# from werkzeug.wrappers import Request,Response
def eg(req,*args,**kwargs):
    if req.method.lower() == "post":
            print(f"REQUEST OBJECT IS ============ {req.body}, POST == {req.POST}")
            for k in req.POST:
                print(req.POST[k])
    form = """
    <form method='post' action='/man'>
        <input type='text' name='first_name' />
        <input type='submit' value='Test Submit' />
    </form>
    """
    return form
class API:
    def __init__(self,app_routes):
        self.routes = app_routes.routes
    
    def __call__(self,environ,start_response):
        req = Request(environ)
        res = self.handle_request(req)
        return res(environ,start_response)
    
    
    def handle_request(self,req):
        
        res = Response()
        handler,handler_ = self.find_handler(req_path=req.path)
        if handler_:
            value=handler(req)
            print("====ec=xecutng value")
            res.text = value
        elif handler_==False:
            res.text = "File not foundr"
        return res
    def find_handler(self,req_path):
        while len(self.routes.keys()) >0:
            for path,handler in self.routes.items():
                if path == req_path:
                    return [handler,True]
            break
        return ["",False]

