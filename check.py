
"""
SYNOPSIS

    TODO check [-h,--help] [-v,--verbose] [--version]

DESCRIPTION

    Checks a page containing opening hours according to http://schema.org and returns "true" if it's within the opening-hours, else false.
    Default page is https://www.oslo.kommune.no/natur-kultur-og-fritid/svommehaller-i-oslo/toyenbadet/

EXAMPLES

    TODO: Show some examples of how to use this script.

EXIT STATUS

    TODO: List exit codes

AUTHOR

    <http://elsykkelevangelisten.no/>

LICENSE

    This script is in the public domain, free from copyrights or restrictions.

VERSION

    $Id$
"""

from rdflib import Graph , Literal, Namespace
from datetime import datetime

url = "https://www.oslo.kommune.no/natur-kultur-og-fritid/svommehaller-i-oslo/toyenbadet/"
schema = Namespace("http://schema.org/")

#Reading rdf from webpage using rdflib; based on code from http://rdflib.readthedocs.org/en/stable/gettingstarted.html
g = Graph()

result = ""
hours = { "opens":[], "closes":[] }

def openOrNot ():

    global options, args, result
    # TODO: Do something more interesting here...
    now = datetime.now()
    g.parse(url)

    id = g.value(predicate = schema.validFrom, object = Literal(str(now.date()), lang='no'))

    for s,p,o in g.triples((id,schema.opens,None)):
        hours["opens"].append(str(o))

    for s,p,o in g.triples((id,schema.closes,None)):
        hours["closes"].append(str(o))

    hours["opens"].sort()
    hours["closes"].sort()


    if len(hours["opens"]) == len(hours["closes"]):
        if len(hours["opens"]) > 1:
            if hours["opens"][1] < str(now.hour):
                if hours["closes"][1] > str(now.hour):
                    result = "Tøyenbadet er åpent!"
                else:
                    result = "Tøyenbadet er stengt!"
        else:
            if hours["opens"][0] < str(now.hour):
                if hours["closes"][0] > str(now.hour):
                    result = "Tøyenbadet er åpent!"
                else:
                    result = "Tøyenbadet er stengt!"
    else:
        print("Noe er galt -- ulikt antall åpnings- og lukketider!")
        # NB! HAr ikke tatt høyde for mer enn to åpnings- og lukketider.


    return result
#    for date in g.objects(None, s.validFrom):
#        if str(date) == str(now.date()):
#            print("%s is today!"%date)



if __name__ == '__main__':
    openOrNot()
    print(result)
    print(hours)
