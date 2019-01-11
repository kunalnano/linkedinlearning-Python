import json
import urllib.request
import prettytable


def printResults(data):

    theJSON = json.loads(data)

    if "name" in theJSON["meta"]["view"]:
        print(theJSON["meta"]["view"]["name"])
    print("----------------\n")

    count = theJSON["meta"]["view"]["downloadCount"]
    print(str(count) + " events recorded")
    print("----------------\n")


def main():
    urldata = "https://data.cityofnewyork.us/api/views/kku6-nxdu/rows.json?accessType=DOWNLOAD"

    webUrl = urllib.request.urlopen(urldata)

    print('result code:' + str(webUrl.getcode()))
    print("----------------\n")

    if (webUrl.getcode() == 200):

        data = webUrl.read()
        printResults(data)
    else:
        print("connection no bueno")


if __name__ == "__main__":
    main()
