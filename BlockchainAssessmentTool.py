from github import Github

# using username and password

# Attention always delete password before committing
# ------------------------------------------------------------------------------
g = Github("krasevi", "xx")
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
repo = g.get_repo("NebulousLabs/Sia")

# stars
print(repo.stargazers_count)

# commits
print(repo.get_commits().totalCount)

# events
print(repo.get_events().totalCount)


# number of contributors
contributors = repo.get_contributors()
contributor_list = []
for contributor in contributors:
    contributors = contributor_list.append(contributor.name)
print(len(contributor_list))


# topics
