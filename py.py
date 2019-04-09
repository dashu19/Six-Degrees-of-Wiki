import requests
import json


S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

dupecheck = {}


def getTitles(title):
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
        if x['title'] not in dupecheck:
            dupecheck[x['title']] = 1
            titles += [x['title']]

    return titles

def getTitlesfromlist(titles):
    ret = []
    for x in titles:
        ret += getTitles(x)
    return ret

##a= getTitles('Albert Einstein')
##print(a)
##b= getTitlesfromlist(a)
##print(b[:10])

def main():
    print('in the main')
    return 0

main()



    

