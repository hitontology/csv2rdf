# reads list of DBpedia classes and outputs sorted list of common classes along with their occurrence
# SELECT DISTINCT(?type) {dbr:Arden_syntax rdf:type ?type.}
from collections import defaultdict
from sys import stdin
import requests
import urllib.parse

classes = defaultdict(set)
count = 0

for resource in stdin:
    count+=1
    resource = resource.strip()
    types = list(requests.get("http://dbpedia.org/sparql?default-graph-uri=http%3A%2F%2Fdbpedia.org&query=SELECT+DISTINCT%28%3Ftype%29+%7Bdbr%3A"+resource+"+rdf%3Atype+%3Ftype.%7D&format=text%2Ftab-separated-values").text.replace('"','').split("\n"))
    types.pop(0) # header
    types = set(types)
    types.remove("");
    #print(types)
    for t in types:
        classes[t].add(resource)

#print(classes)
sorted = sorted(classes.keys(), key=lambda k: -len(classes[k]))
sorted = sorted[:11]
for k in sorted:
    quote = urllib.parse.quote_plus(k)
    query = "https://dbpedia.org/sparql?default-graph-uri=http%3A%2F%2Fdbpedia.org&query=SELECT+COUNT%28DISTINCT%28%3Fx%29%29+%7B%3Fx+a+%3C"+quote+"%3E+%7D&format=text%2Ftab-separated-values&CXML_redir_for_subjs=121&CXML_redir_for_hrefs=&timeout=30000&debug=on&run=+Run+Query+"
    size = int(requests.get(query).text.split("\n")[1])
    print("|",k,"|",len(classes[k]),"|",size,"|",len(classes[k])*100/size,"|")
    #print(k+";"+len(classes[k])+";"+size+";"+classes[k])
print(count,"resources in total")

