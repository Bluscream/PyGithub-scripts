from github import Github, GithubException
username = ""; password = ""; token = ""
from credentials import username, password, token
headers = { 'Authorization': "Bearer %s"%token,'Cache-Control': "no-cache" }

g = Github(username, password)
# g = Github(token)

repos = 0
processed = 0
# referrers = {}
me = g.get_user()
for repo in me.get_repos():
    repos += 1
    failed = False
    repo_str = "Repository: %s [repo_dl]"%repo.full_name
    repo_downloads = 0
    releases = repo.get_releases()
    try:
        for release in releases:
            repo_str += "\n\tRelease: %s (%s) [release_dl]"%(release.title, release.tag_name)
            assets = release.get_assets()
            release_downloads = 0
            for asset in assets:
                release_downloads += asset.download_count
                repo_str += "\n\t\tAsset: %s [%s]" % (asset.name, asset.download_count)
            repo_str = repo_str.replace("release_dl", str(release_downloads))
            repo_downloads += release_downloads
    except GithubException:
        failed = True
        pass
    repo_str = repo_str.replace("repo_dl", str(repo_downloads))
    print(repo_str)
    if not failed: processed += 1
print("Repositories processed: %s / %s"%(processed, repos))
