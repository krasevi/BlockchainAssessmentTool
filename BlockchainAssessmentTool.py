from github import Github

# using username and password

# Attention always delete password before committing
# ------------------------------------------------------------------------------
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
    # print(dir(repo))

# define repository
repo = g.get_repo("krasevi/BlockchainAssessmentTool")


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
additions = code_frequency[-1].additions
deletions = code_frequency[-1].deletions
week = code_frequency[-1].week
print (additions, deletions, week)

# number of contributors
contributors = repo.get_contributors()
contributor_list = []
for contributor in contributors:
    contributors = contributor_list.append(contributor.name)
print(len(contributor_list))
