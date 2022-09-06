class Router:
    routes = {}
    def __init__(self):
        pass
    
    def route(self,path,component):
        # to be updated for class and functional components
        self.routes[path] = component
