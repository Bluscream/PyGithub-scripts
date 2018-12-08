from github import Github
username = ""; password = ""; token = ""
from credentials import username, password, token

g = Github(username, password)
# g = Github(token)

repos = 0
processed = 0
me = g.get_user()
for repo in me.get_repos():
    repos += 1
    failed = False
    try:
        repo.edit(private=False)
        print(repo.name,"is now public")
    except:
        failed = True
        print("Failed to make",repo.full_name,"public!")
    if not failed: processed += 1
print("Repositories processed: %s / %s"%(processed, repos))