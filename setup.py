from setuptools import setup, find_packages
desc = """
## HOTWEB WEB FRAMEWORK
Python web framework for designing lucrative websites in python programming language. The goal of HOTWEB FRAMEWORK 
is to allow developers to develope websites in one language, that is python because you can do anything using Python Programming language

## Author
```{py}
Real Manlow (aka ManlowCharumbira)
```
## Contacts
instagram.com/realmanlow
realmanlow20@gmail.com
charumbiramanlow20@gmail.com
"""
def readme():
    with open("readme.md","r") as f:
        info = f.read()
        return info
setup(
    name="hotweb",
    version="0.7.189",
    license="MIT",
    author = "Real Manlow,aka ManlowCharumbira",
    long_description=desc,
    long_description_content_type="text/markdown",
    author_email="realmanlow20@gmail.com",
    packages=find_packages(),
    #package_dir = {'':'hotweb'},
    include_package_data = True,
    keywords = "hotweb python-web-framework python web framework fast light secure",
    install_requires = [
        "parse","waitress","webob","requests","hotweb-cli","whitenoise","Werkzeug","Jinja2","hotweb-cli"
    ]
)