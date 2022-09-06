from .allWidgets.headContent import HeadContent
from .allWidgets.body import BodyContent
from .allWidgets.footer import Footer

class SiteWrapper:
    def __init__(self):
        self.head_ = ""
        self.body_ = ""
        self.footer_ = ""

    
    def head(self,title="Document",files=[]):
        head = HeadContent(files=files)
        self.head_ = head.head(title)
    
    def body(self,files=[],content="Hello World"):
        body = BodyContent(files=files)
        self.body_ = body.body(content=content)
    def footer(self,content="Brought  To You With Love from HotWeb",files=[]):
        footer = Footer()
        self.footer_ = footer.footer(content=content,files=files)
    
    def web_document(self,req,res):
        if len(self.head_) ==0:
            self.head()
        if len(self.body_) ==0:
            self.body()
        if len(self.footer_) ==0:
            self.footer()
        
        doc = self.head_ + "\n" + self.body_ + "\n" + self.footer_
        res.text = doc
        print(doc)
        #return doc

