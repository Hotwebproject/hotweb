class Form:
    
    def __init__(self,component="form",**kwargs):
        self.kwargs = kwargs
        self.component =component
        self.has_closing = True
        self.current_component = f"< {self.component} "
        self.current_end ='\n' + f"</{self.component}>"
        #self.current_component = current_component + self.current_end
    def __call__(self,component):
        print("============inside call")
        self.define_component(component)
        self.build_component()
    # append child element to the current component
    def add_child(self,child):
        # slice from the closing tag to append the child before closing tag
        end_len = len(self.current_end)
        self.current_end =  '\n' + child + self.current_end
    # remove child element to the current component,can get help from javascript
    def remove_child(self,child):
        pass
    def add_class(self):
        pass
    def remove_class(self):
        pass
    # declare type of component to be built
    def define_component(self,component,has_closing=True):
        # to be updated to validate types of components entered
        self.has_closing = has_closing
        self.component = component
        return self.component
    # now building the component and its attributes
    def build_component(self):
        # content of the html component
        content = ""
        has_class = False
        attributes = ''
        for attr,value in self.kwargs.items():
            if attr == "content":
                content = content + attr
                continue
            if attr == "class_":
                attributes += f'class="{self.component}__class component_class {value}" '
                has_class = True
                continue
            attributes = attributes + ' ' + f'{attr}="{value}" '
        if not has_class:
            attributes += f'class="{self.component}__class" '
        if self.has_closing:
             self.current_component = self.current_component + attributes + " >" + "\n" + content + "\n" + self.current_end
             return self.current_component
        else:
            self.current_component = self.current_component + attributes + " />" + "\n"
            return self.current_component

def Button():
    return "<div>INSIDE A DIV ELEMENT</div>"
form = Form(method="post",action="localhost/posts",class_="hello test class")
form.add_child(Button())
form.add_child("<div>INSIDE A DIV ELEMENT</div> \n")
print(form.build_component())
text = "</manlow"
#text[2] = text[2] + "b"
#t1 = text[1:2]
#print(text[-1:].split(" </"))
print()