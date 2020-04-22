import requests
from sys import stdin

for line in stdin:
    if (requests.get("https://www.snik.eu/sparql?default-graph-uri=&query=ASK+%7Bbb%3A"+line+"+%3Fp+%3Fo.%7D&should-sponge=&format=text%2Fhtml&timeout=0&debug=on").json() == False):
        print(line.strip())
