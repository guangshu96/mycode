#!/usr/bin/phthon3

import urllib.request
import json
import webbrowser
from pprint import pprint as pp

#apodurl = 'https://api.nasa.gov/planetary/apod?'
#mykey = 'api_key=FTZKEdwjAKuKFqcWmXHahVgSN8eSs8vzs968nzTJ'


NASAAPI = 'https://api.nasa.gov/planetary/apod?'
mykey = 'api_key=FTZKEdwjAKuKFqcWmXHahVgSN8eSs8vzs968nzTJ'


#apodurlobj = urllib.request.urlopen(apodurl + mykey)
#
#apodread = apodurlobj.read()
#
#decodeapod = json.loads(apodread.decode('utf-8'))
#
#print("\n\nConverted python data")
#print(decodeapod)
#
#
#input('\nPress enter to open NASA pic of the day in firefox')


def main():
    
    nasaapiobj = urllib.request.urlopen(NASAAPI + mykey)
    nasaread = nasaapiobj.read()
    convertedjson = json.loads(nasaread.decode('utf-8'))
    print(convertedjson)
    input('\nThis is converted json, press enter to continue.')

    pp(convertedjson)
    input('\nPress enter to view this poto of the day')


    print(convertedjson['explanation'])
    input('\nPress Enter to view this photo of the day')


    webbrowser.open(convertedjson['hdurl'])


main()
