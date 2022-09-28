class Router:
    routes = {"/404":{"404":"4040 page","compo":6}}
    def __init__(self):
        pass
    """
    later on to handle dynamic urls   
    """
    def route(self,path,component,static = None,prefix=None):
        # to be updated for class and functional components
        self.routes[path] = {}
        self.routes[path][path] = component
        self.routes[path]["static"] = static
        self.routes[path]["prefix"] = static
                

