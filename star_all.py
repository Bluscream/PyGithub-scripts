from github import Github
username = ""
password = ""
token = ""
from credentials import username, password, token

g = Github(username, password)
# g = Github(token)

repos = 0
processed = 0
me = g.get_user()
for repo in me.get_repos():
    repos += 1
    failed = False
    str = ""
    try:
        me.add_to_starred(repo)
        str += "Starred, "
    except:
        failed = True
        str += "Failed to star, "
    try:
        me.add_to_subscriptions(repo)
        str += "Subscribed, "
    except:
        failed = True
        str += "Failed to subscribe, "
    try:
        me.add_to_watched(repo)
        str += "Watched, "
    except:
        failed = True
        str += "Failed to watch, "
    print(repo.full_name, ":", str )
    if not failed: processed += 1
print("Repositories processed: %s / %s"%(processed, repos))