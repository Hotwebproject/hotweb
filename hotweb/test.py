from .engine.views.all import SiteWrapper
from .engine.routing.Route import Router
from .engine.routing.index import app
from .engine.routing.waitress_server import run_server
from webob import Response
resp = Response()

st = SiteWrapper()
ec = st.web_document
route = Router()
def view(req,res):
    res.text = "hello world test"
#route.route("/test",st.web_document)
route.route("/test",view)
#app = API()
run_server(app)
