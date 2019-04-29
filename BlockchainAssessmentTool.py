# author: Severin Kranz
# GitHub: https://github.com/krasevi

# ******************************************************************************
# prerequisites
# ******************************************************************************
# 1. install pyGithub by using "pip install pyGithub" in the command line

from github import Github
import datetime

# ******************************************************************************
# settings
# ******************************************************************************

# using username and password
# Attention always delete password before committing to GitHub
g = Github("krasevi", "xxx")
# or using an access token
# g = Github("access_token")
# Github Enterprise with custom hostname
# g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")
# repository
repositoryName = "input-output-hk/rust-cardano"
# active developer definition
minContributions = 50
activeDevDays = 30

# ******************************************************************************
# 1. Statistics per repository
# ******************************************************************************

# define repository
repo = g.get_repo(repositoryName)

# stars
stars_totalCount = repo.stargazers_count
print("stars: " + str(stars_totalCount))

# events
events = repo.get_events()
events_totalCount = events.totalCount
print("events: " + str(events_totalCount))

# forks
forks = repo.get_forks()
forks_count = repo.forks_count
forks_totalCount = forks.totalCount
print("forks: "+ str(forks_count))
print("forks: "+ str(forks_totalCount))

# commits
commits = repo.get_commits()
commit_totalCount = commits.totalCount
print("commits: " + str(commit_totalCount))

# watchers
watchers_count = repo.watchers_count
watchers = repo.get_subscribers()
watchers_totalCount = watchers.totalCount
print("watchers: " + str(watchers_totalCount))
print("watchers: " + str(watchers_count))

# number of pull requests
pulls = repo.get_pulls()
pulls_numbers_list = []
for pull in pulls:
    pulls_numbers_list.append(pull.number)
pulls_totalCount = len(pulls_numbers_list)
print("pulls: " + str(pulls_totalCount))

# number of contributors
contributors = repo.get_contributors()
contributor_list = []
contributions_list = []

for contributor in contributors:
    contributor_list.append(contributor.name)
    contributions_list.append(contributor.contributions)
contributor_totalCount = len(contributor_list)
print("number of contributors: " + str(contributor_totalCount))


# commit_activity
# Get the last year of commit activity data grouped by week
# probably only commits by owners are counted - tbd
commit_activity_stats = repo.get_stats_commit_activity()
commit_activity_list_week = []
commit_activity_list_days = []
for StatsCommitActivity in commit_activity_stats:
    commit_activity_stats = commit_activity_list_week.append(StatsCommitActivity.total)
    commit_activity_stats = commit_activity_list_days.append(StatsCommitActivity.days)

# commit_activity last week
print("commit activity last week: " + str(commit_activity_list_week[-1]))
print("commit activity daily: " + str(commit_activity_list_days[-1]))

# commit_activity last changes_month
month = [-1, -2, -3, -4]
commit_activity_month = sum(int(commit_activity_list_week[i]) for i in month)
print("commit activity last month: " + str(commit_activity_month))


# code_frequency
# Get the number of additions and deletions per week
# probably only gets code frequency of owners - tbd
code_frequency = list(repo.get_stats_code_frequency())

# code_frequency in the last week
week = code_frequency[-1].week
additions_week = int(code_frequency[-1].additions)
deletions_week = int(code_frequency[-1].deletions)
changes_week = abs(additions_week)+abs(deletions_week)
print("additions last week: " + str(additions_week))
print("deletions last week: " + str(deletions_week))
print("changes last week: " + str(changes_week))

#  code_frequency in the last month
month = [-1, -2, -3, -4]
additions_month = sum(int(code_frequency[i].additions) for i in month)
deletions_month = sum(int(code_frequency[i].deletions) for i in month)
changes_month = abs(additions_month) + abs(deletions_month)
print(additions_month, deletions_month, changes_month)
print("additions last month: " + str(additions_month))
print("deletions last month: " + str(deletions_month))
print("changes last month: " + str(changes_month))


# ******************************************************************************
# 2. statistics for active developers
# ******************************************************************************

# define active developers per repository

# active developers
activeDevs = []
for i in range(contributor_totalCount):
    if int(contributions_list[i]) > minContributions:
        activeDevs.append(contributor_list[i])
        i += 1
    else:
        i += 1

# for i in range(activeDevs)
# commits to a repo
commits = repo.get_commits()
# commits_sha_list = []
commit_author_dates = []
commit_author_names = []

activeDevsInPeriod = []

for commit in commits:
    if commit.commit.author.name not in activeDevsInPeriod:
        if commit.commit is not None:
            if commit.commit.author.date >= (datetime.datetime.now()- datetime.timedelta(days=activeDevDays)):
                commit_author_names.append(commit.commit.author.name)
                if commit.commit.author.name in activeDevs:
                    activeDevsInPeriod.append(commit.commit.author.name)
    else:
        pass
print("active Developers: " + str(activeDevsInPeriod))

        # if commit.commit.author.date >= (datetime.datetime.now()- datetime.timedelta(days=1)):
        #    commit_author_dates.append(commit.commit.author.date)
        #    commit_author_names.append(commit.commit.author.name)
        #    commit_author_id.append(commit.commit.author.id)

# print(commit_author_dates)
#     commits_sha_list.append(commit.sha)
# print("commits to repo: " +str(len(commits_sha_list)))

# print("active developer ids: " + str(activeDevs))
