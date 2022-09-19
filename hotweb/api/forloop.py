class ForLoop:
    
    def __init__(self,loop_struct,**kwargs):
        self.kwargs = kwargs
        self.component ="component"
        self.has_closing = True
        self.current_component = "{% for "+f"{loop_struct}"+" %}"
        self.current_end ='\n' + "{% endfor %}"
        #self.current_component = current_component + self.current_end
    def __call__(self,component):
        print("============inside call")
        self.build_component()
    # append child element to the current component
    def add_child(self,child):
        print("===inside button compnent======")
        # slice from the closing tag to append the child before closing tag
        end_len = len(self.current_end)
        self.current_end =  '\n' + child + self.current_end
        print("===exit button compnent======")
    # now building the component and its attributes
    def build_component(self):
        # content of the html component
        self.current_component = self.current_component + self.current_end
        return self.current_component

def Button(arg):
    #print("===inside button compnent======")
    return f"<div>INSIDE A DIV ELEMENT {arg}</div>"
form = ForLoop("student in students")
form.add_child(Button("{{student.name}}"))
form.add_child("<div>INSIDE A DIV ELEMENT last one</div> \n")
print(form.build_component())
print()