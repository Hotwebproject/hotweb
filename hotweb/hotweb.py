from server import render
from shortcuts.load_file import current_dir
from router.route_ import Router
print(current_dir)
import os
output = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="assets/test.css">
</head>
<body>
  <h1>Manlow</h1>  
  <img src='/assets/section.PNG' alt='hello' />
</body> 
</html>
"""
def eg(req):
    return "hello from manlow"
app = Router()
def hel(req):
    img = os.path.join(os.getcwd(),"router","section.png")
    
    print(os.getcwd())
    return output #"<h1>Hello There</h1>" + "<br>" + f"<img src='/assets/section.PNG' alt='hello' />"
app.route("/",hel)
app.route("/hello",eg)
render(app)