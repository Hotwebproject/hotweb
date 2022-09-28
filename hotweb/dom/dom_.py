class Dom:
    js_template = ""
    def __init__(self):
        pass
    
    def click(self,class_id,fn):
        pass
    def write_to_js(self,js=""):
        with open("dom.js","w") as f:
            file = self.generate_js_file(js)
            f.write(file)
    def generate_js_file(self,js):
        start = """
        $(document).ready(function(){
        """
        end = "\n \t" + "})"
        if len(js)>0:
            end = js + "\n" + end
        content = start + end
        return content
    def removeClass(self,klass):
        pass

d = Dom()
#d.write_to_js("// d instance call")
#e = Dom()
#e.write_to_js("// e instance call")
import inspect
clk = str(inspect.getsource(d.click))
print(clk + "\t hello")

"""
/* 
         the json file keeps track of two values
         1. commited state=> this means content was written to js
         2. to_commited state
*/
"""