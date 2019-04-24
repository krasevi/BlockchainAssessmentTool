from github import Github



# Attention always delete password before committing
# ------------------------------------------------------------------------------
# using username and password
g = Github("krasevi", "xxx")
# or using an access token
# g = Github("access_token")
# Github Enterprise with custom hostname
# g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")
# ------------------------------------------------------------------------------

# get repository names of chosen user
# for repo in g.get_user().get_repos():
    # print(repo.name)
    # repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    # print(dir(repo)

# ******************************************************************************
# 1. Statistics per repository
# ******************************************************************************

# define repository
repo = g.get_repo("openshift/installer")

# stars
starCount = repo.stargazers_count
print(starCount)

# commits
commits = repo.get_commits()
commitCount = commits.totalCount
print(commitCount)

# events
events = repo.get_events()
eventCount = events.totalCount
print(eventCount)

# forks
forks = repo.get_forks()
forkCount = forks.totalCount
print(forkCount)

# stats
stats = repo.get_stats_code_frequency()
code_frequency = list(stats)

# stats last week
week = code_frequency[-1].week
additions_week = int(code_frequency[-1].additions)
deletions_week = int(code_frequency[-1].deletions)
changes_week = abs(additions_week)+abs(deletions_week)
print(week, additions_week, deletions_week, changes_week)

# stats last month
month = [-1, -2, -3, -4]
additions_month = sum(int(code_frequency[i].additions) for i in month)
deletions_month = sum(int(code_frequency[i].deletions) for i in month)
changes_month = abs(additions_month) + abs(deletions_month)
print(additions_month, deletions_month, changes_month)

# number of contributors
contributors = repo.get_contributors()
contributor_list = []
for contributor in contributors:
    contributors = contributor_list.append(contributor.name)
contributorCount = len(contributor_list)
print(contributorCount)
