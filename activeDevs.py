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

myuser = input("enter github username: ")
mypassword = input("enter github password: ")
g = Github(myuser, mypassword)
# or using an access token
# g = Github("access_token")
# Github Enterprise with custom hostname
# g = Github(base_url="https://{hostname}/api/v3", login_or_token="token")

# repository
repositoryName = "input-output-hk/rust-cardano"
# define repository
repo = g.get_repo(repositoryName)

# active developer definition
# define number of minimum contributions of a developer to be considered active
minContributions = 50
# define time frame in which the developer made his last commit (to be active)
activeDevDays = 30


# ******************************************************************************
# 2. statistics for active developers
# ******************************************************************************

print("repository: " + str(repo.name))

# number of contributors
contributors = repo.get_contributors()
contributor_list = []
contributions_list = []
dev_dict = {}

for contributor in contributors:
    contributor_list.append(contributor.name)
    contributions_list.append(contributor.contributions)
    dev_dict[contributor.name] = contributor.contributions
contributor_Count = len(contributor_list)
print("contributor count: " + str(contributor_Count))
# print(dev_dict)


# activeDevs = []
activeDev_dict = {}
for i in range(contributor_Count):
    if int(contributions_list[i]) > minContributions:
        # activeDevs.append(contributor_list[i])
        activeDev_dict[contributor_list[i]] = contributions_list[i]
        i += 1
    else:
        i += 1
print("active dev count: " + str(len(activeDev_dict)))

# get commits to the repo
commits = repo.get_commits()

# get active developers that commited in a certain time frame
activeDevsInPeriod = []
commit_author_names = []
activeDevsInPeriod_logins = []

for commit in commits:
    # check if developer is already in the list
    if commit.commit.author.name not in activeDevsInPeriod:
        # sort out empty commits
        if commit.commit is not None:
            # sort out commits older than x days
            if commit.commit.author.date >= (datetime.datetime.now() -
                    datetime.timedelta(days=activeDevDays)):
                    commit_author_names.append(commit.commit.author.name)
                    # sort out devs that do not fulfill min. number of commits
                    # if commit.commit.author.name in activeDevs:
                    if commit.commit.author.name in activeDev_dict:
                        activeDevsInPeriod.append(commit.commit.author.name)
                        activeDevsInPeriod_logins.append(commit.author.login)
    else:
        pass
print("list of active devs: " + str(activeDevsInPeriod_logins) + "\n")

# get statistics for active developers
print("statistics: \n")

i = 0
devStars = 0
for i in range(len(activeDevsInPeriod_logins)):
    dev = activeDevsInPeriod_logins[i]
    user = g.get_user(dev)
    print("username: "+str(dev))
    print("name: " + str(user.name))
    print("contributions to repo: " + str(activeDev_dict[user.name]))
    print("public repo count: " + str(user.public_repos))
    print("follower count: " + str(user.followers))
    print("following other repos: " + str(user.following))
    repositories = g.search_repositories(query='user:'+str(dev))
    repoCount = 0
    for repo in repositories:
        devStars = devStars + int(repo.stargazers_count)
        repoCount += 1
    print("Repository Count: " + str(repoCount))
    print("star count: " + str(devStars))
    print("\n")
    i += 1
