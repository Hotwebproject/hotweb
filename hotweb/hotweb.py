from server import render
from shortcuts.load_file import current_dir
from router.route_ import Router
print(current_dir)
import os
app = Router()
def hel(req):
    img = os.path.join(os.getcwd(),"router","section.png")
    print("=====App Mounted=======")
    print(os.getcwd())
    return "<h1>Hello There</h1>" + "<br>" + f"<img src='/router/section.png' alt='hello' />"
app.route("/",hel)
render(app)