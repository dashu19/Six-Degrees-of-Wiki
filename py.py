import requests

print("Hello World!")

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

Params = {
    "action": "query",
    "format": "json",
    "titles": "Albert Einstein",
    "prop": "links",
    }

R = S.get(URL, params = Params)
Data = R.json()

Key = list(Data["query"]['pages'].keys())

print(Key)

Data = Data["query"]['pages'][Key[0]]['links']

titles = []

for x in Data:
    print(x['title'])
    titles += [x['title']]

print(titles)
