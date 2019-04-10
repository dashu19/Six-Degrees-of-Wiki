import requests
import json

#   This will be a small Python app that asks the user for a starting point and and end point, to see if
#   two wikipedia pages are connected within 6 "degrees".
#


S = requests.Session()
URL = "https://en.wikipedia.org/w/api.php"

#dupecheck = {} #hm... need a new dupe check for each query, reinstantiate function?

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

def getStart():
    """Asks user for input that will be passed in as a title parameter
        Needs error checking capabilities
    """
    while True:
        ret = input("Enter a starting point: ")
        if checkTitle(ret):
            return ret
        else:
            print("Try again!")
            continue

def getEnd():
    """Asks user for input that will be passed in as a title parameter
        Needs error checking capabilities
    """
    while True:
        ret = input("Enter a ending point: ")
        if checkTitle(ret):
            return ret
        else:
            print("Try again!")
            continue
    


def getTitles(title, dupecheck):
    rparams = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "links",
        #"pllimit": 'max'
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

    return [titles, dupecheck]

def getTitlesfromlist(titles, dupecheck):
    ret = []
    for x in titles:
        ret += getTitles(x, dupecheck)[0]
    return ret

def query():
    dupecheck = {}
    start = getStart()
    end = getEnd()

    a = getTitles(start, dupecheck)
    b = getTitlesfromlist(a[0], a[1])
    print(a)
    print(b)
    return 0
    

##a= getTitles('Albert Einstein')
##print(a)
##b= getTitlesfromlist(a)
##print(b[:10])

def main():
    print('in the main')
    print('Welcome!')
    print("Let's see if two Wikipedia pages are within 6 degrees of each other!")
    while True:
        
        break
    return 'lmao'

main()



    

