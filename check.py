
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

hours = { "opens":[], "closes":[] }

def main ():

    global options, args
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

    if hours["opens"][0] < str(now.hour):
        if hours["closes"][0] > str(now.hour):
            print("Tøyenbadet er åpent!")
        else:
            print("Tøyenbadet er stengt!")

#    for date in g.objects(None, s.validFrom):
#        if str(date) == str(now.date()):
#            print("%s is today!"%date)

    print(hours)


if __name__ == '__main__':
    main()
