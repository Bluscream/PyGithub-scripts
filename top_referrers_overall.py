from github import Github, GithubException
from requests import request
from collections import OrderedDict
from json import dumps
token = ""
from credentials import token
headers = { 'Authorization': "Bearer %s"%token,'Cache-Control': "no-cache" }

g = Github(token)

repos = 0
referrers = {}
me = g.get_user()
for repo in me.get_repos():
    repos += 1
    referers_ = request("GET", "https://api.github.com/repos/%s/%s/traffic/popular/referrers"%(me.name, repo.name), headers=headers).json()
    if not isinstance(referers_, list):
        continue
    for referrer in referers_:
        name = referrer['referrer']
        if not name in referrers.keys():
            referrers[name] = 0
        referrers[name] += referrer['count']
        print(referrers)
    # if repos > 3: break
print("Repositories processed:",repos)
asdict = OrderedDict(sorted(referrers.items()))
print(asdict)
asjson = dumps(asdict)
print(asjson)