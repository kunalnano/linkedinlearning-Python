import json
import urllib

def main():
    urldata = ""https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson""

    webUrl = urllib.request.urlopen(urldata)
