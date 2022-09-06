class BodyContent:
    def __init__(self,files=[]):
       pass
    
    def body(self,content="Hello World"):
        open_tag = "\n" + "<body>" + "\n"
        open_tag = open_tag + content
        return open_tag