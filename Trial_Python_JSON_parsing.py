# Import JSON and urllib.request module

import json
import urllib.request
import prettytable

# Create a function printResults to store parsed json using 'loads' method using features found in json key value pair data from usgs website


def printResults(data):

    theJSON = json.loads(data)

    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

    count = theJSON["metadata"]["count"]
    print(str(count) + " events recorded")

    for i in theJSON["features"]:
        print(i["properties"]["place"])
    print("------------------\n")

    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
    print("------------------\n")

# Main function to load url data from usgs website


def main():

    urldata = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

# Error handling option to first check if you can connect to the website

    webUrl = urllib.request.urlopen(urldata)
    print('result code: ' + str(webUrl.getcode()))
    if (webUrl.getcode() == 200):

# If no error found read the webUrl data and store results in printResults(data)

        data = webUrl.read()
        printResults(data)
    else:
        print("Received error, cannot parse results")


if __name__ == "__main__":
    main()

x = prettytable()

x.field_names(["properties"]["mag"], ["features"]["place"])

print(x)
