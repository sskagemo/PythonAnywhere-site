
# Based on the simple Flask Hello World app ...

from flask import Flask
from check import openOrNot

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

teller = 0

#Reading rdf from webpage using rdflib; based on code from http://rdflib.readthedocs.org/en/stable/gettingstarted.html
#g = rdflib.Graph()

@app.route('/')
def hello_world():

    global teller
    teller+=1

    #g.remove((None,None,None))
    #g.parse("https://www.oslo.kommune.no/natur-kultur-og-fritid/svommehaller-i-oslo/toyenbadet/")

    #svar = "Det er " + str(len(g)) + " tripler på siden om Tøyenbadet, og det har du spurt om " + str(teller) + " ganger."

    return htmldocStart + openOrNot() + htmldocEnd
    #return openOrNot()
    #'Hello from Flask!'

@app.route('/Agathe-og-Simon')
def hei_dere():
    return """<html><head></head><body><p>Dere er verdens beste! Jeg <blink><strong>digge-digge-digge-digge-digger</strong></blink> dere! Stolt hilsen pappaen deres. Og <a href="/mamma">mammaen deres</a> også!</p></body></html>"""

@app.route('/mamma')
def hei_mamma():
    return """<html><head></head><body><p>Mamma er best, ingen protest - den som står imot, må spise gulrot</p></body></html>"""