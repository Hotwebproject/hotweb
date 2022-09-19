import os

current_dir = os.getcwd()
#print(f"=={current_dir}")
def load(path):
    new_dir = os.chdir(path)
    #print(new_dir)
    file = os.path.join(str(os.getcwd()),"views","all.py")
    print(file)
    print("The new path====",os.getcwd())
#print(dir(os))
#load("../engine/views")
#print(f"=={current_dir}")

#print(dir(os.path.dirname))
print(os.path.dirname(os.path.join(str(os.getcwd()),"views","all.py")).split(os.path.sep))