import json
import urllib.request
import prettytable


def printResults(data):

    theJSON = json.loads(data)

    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

        count = theJSON["metadata"]["count"]
        print(str(count) + " events recorded")

        for i in theJSON["features"]:
            print(i["properties"], ["place"])
        print("----------------------\n")

        for i in theJSON["features"]:
            if i["properties"]["mag"] >= 4.0:
                print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
        print("----------------------\n")


def main():
    urldata = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    webUrl = urllib.request.urlopen(urldata)

    print('result code:' + str(webUrl.getcode()))

    if (webUrl.getcode() == 200):

        data = webUrl.read()
        printResults(data)
    else:
        print("connection no bueno")


if __name__ == "__main__":
    main()
