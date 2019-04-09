import requests
import json

#   This will be a small Python app that asks the user for a starting point and and end point, to see if
#   two wikipedia pages are connected within 6 "degrees".
#

#check

S = requests.Session()
URL = "https://en.wikipedia.org/w/api.php"

dupecheck = {} #hm... need a new dupe check for each query

def checkTitle(title):
    """Takes string represeting pages title parameter, and checks if it is a valid page title"""
    
    rparams = {
        "action": "query",
        "format": "json",
        "titles": title,
    }

    R = S.get(URL, params = rparams)
    Data = R.json()
    mykey = list(Data["query"]['pages'].keys())[0]
    if mykey == '-1':
        return False
    else:
        return True
    
    


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
    mykey = list(Data["query"]['pages'].keys())[0]

    Data = Data["query"]['pages'][mykey]['links']
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
    while True:
        #dostuff
        break
    return 'lmao'

main()



    

