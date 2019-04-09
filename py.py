import requests
import json


S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

dupecheck = {}


def getlinkstitles(title):
    rparams = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "links",
        "pllimit": 'max'
    }

    R = S.get(URL, params = rparams)
    Data = R.json()
    mykey = list(Data["query"]['pages'].keys())

    Data = Data["query"]['pages'][mykey[0]]['links']
    titles = []

    for x in Data:
        titles += [x['title']]

    return titles

def childrensearch(titles):
    ret = []
    for x in titles:
        ret += getlinkstitles(x)
    return ret



    

