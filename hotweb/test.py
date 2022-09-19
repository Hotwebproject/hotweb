from dom.dom_ import Dom
import inspect
d = Dom()
clk = str(inspect.getsource(d.generate_js_file))
clk = clk.replace(":","{")
clk = clk.replace("def","function")
clk = clk + "}"
with open("test.txt","w") as f:
    f.write(clk)
print(clk)