
class Router:
    routes = {}
    def __init__(self):
        pass
    def route(self,path,component):
        #for path_ in self.routes.keys():
            #if path_ == path:
                #print("===========path taken========")
                #return
        # component is the view of the given page path
        self.routes[path] = component
    
    def get_routes(self):
        return self.routes
    
    #def example_handler(self,req,res,**args,**kwargs):
        #res.text = "Entry or Home Handler executed"

#app =Router()
#app.route("/home","this is home page")
#app.route("/aboute","this is home page")
#app.route("/services","this is home page")
#print(app.get_routes())