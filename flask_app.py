
# Based on the simple Flask Hello World app ...

from flask import Flask
import rdflib

app = Flask(__name__)

htmldocStart = """
<html>
<head>
<title>Er Tøyenbadet åpent?</title>
<link rel="stylesheet" type="text/css" href="/s/standard.css" />
</title>
<body>
"""
htmldocEnd = """
</body>
</html>
"""

#Reading rdf from webpage using rdflib; based on code from http://rdflib.readthedocs.org/en/stable/gettingstarted.html
g = rdflib.Graph()
g.parse("https://www.oslo.kommune.no/natur-kultur-og-fritid/svommehaller-i-oslo/toyenbadet/")

@app.route('/')
def hello_world():

    svar = "Det er " + str(len(g)) + " tripler på siden om Tøyenbadet"

    return htmldocStart + svar + htmldocEnd
    #'Hello from Flask!'

