from webob import Request, Response
from .Route import Router
from .utils import default_response
#from ....app.app import run
class API:
    

    def __init__(self):
        router = Router()
        #self.collect_routes()
        self.routes = {}
        self.routes = router.get_routes()
        self.routes["/testss"] = self.collect_routes
    
    # main application call
    def __call__(self,environ,start_response):
        req = Request(environ)

        res = self.handle_requests(req)
        #res = Response()
        #res.content_type = "text/html"
        #res.text = "Hello, World" + "\n" + "<h1 style='background-color:red;color:white;'>MANLOW CHARUMBIRA </h1>"
        #print(f"=======request object path======{req.path}, method====={req.method}")
        print(f"=======routes======{self.routes}")
        #return res(environ,start_response)
    # collect website routes, import the app module and run the Run function in it
    def collect_routes(self,req,res):
        res.text = "hello"
    def handle_requests(self,request):
        found = False
        res = Response()
        while len(self.routes) >0:
            for path,handler in self.routes.items():
                if path == request.path:
                    print(f"===match found====path--{request.path}, handler==={handler},routes=={self.routes}")
                    handler(request,res)
                    #res.text = handler
                    found = True
                    return res
        if not found:
            default_response(res)
        
app = API()