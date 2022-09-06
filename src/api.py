from webob import Response,Request
import time
from routes import Router
def eg(req,res):
    found = f"found 1"
    count = "0"
    for k in range(1,10):
        if k%10 ==0:
            count = count + str(int(count)+1)
            found = found + "<script>console.log('nor-manlow')</script> k==0 \n" + str(count)
            res.text = found 
            #time.sleep(5)
        else:
            #f"test :k=={k}: modulo not zero=========" + window.location='nor-manlow' window.location='manlow' document.title = 'the doc' 
            count = count + str(int(count)+1)
            res.text =  "<body><script>console.log('manlow');document.title = 'the doc'</script> k <>==0</body> \n"+ str(count)
            #time.sleep(10)
class API:
    def __init__(self):
        self.routes = {"/":eg}
    
    def __call__(self,environ,start_response):
        req = Request(environ)
        res = self.handle_request(req)
        print(f"res====={res}")
        #res.text = "hello"
        return res(environ,start_response)
    
    
    def handle_request(self,req):
        res = Response()
        handler,handler_ = self.find_handler(req_path=req.path)
        if handler_:
            handler(req,res)
        else:
            res.text = "File not foundr"
        return res
    def find_handler(self,req_path):
        while len(self.routes.keys()) >0:
            for path,handler in self.routes.items():
                if path == req_path:
                    return [handler,True]
            break
        return ["",False]

app = API()