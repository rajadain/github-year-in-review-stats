import sys

from github import Github
from datetime import datetime

token = ''

with open('token.txt', 'r') as tokenfile:
    token = tokenfile.read().replace('\n', '')

if not token:
    sys.exit('No token specified')

g = Github(token)

authenticated_user = g.get_user()
# Get named_user from authenticated_user, needed for some API calls
# https://github.com/PyGithub/PyGithub/issues/330
named_user = g.get_user(authenticated_user.login)

since = datetime(2018, 1, 1)

# Initialize counters. Unfortunately, I could not find a way in the API to
# fetch pull requests created by a user
issues_assigned = (authenticated_user
                   .get_user_issues(since=since, state='all')
                   .totalCount)
issues_created = 0
repos = []
commits = 0
lines_added = 0
lines_removed = 0

rs = authenticated_user.get_repos()
for r in rs:
    try:
        # Count created issues
        cis = r.get_issues(since=since, creator=named_user).totalCount
        if cis:
            issues_created += cis
            if r not in repos:
                repos.append(r)

        # Count commits and changed lines
        cs = r.get_commits(since=since, author=authenticated_user)
        if cs.totalCount:
            if r not in repos:
                repos.append(r)

            for c in cs:
                commits += 1
                lines_added += c.stats.additions
                lines_removed += c.stats.deletions
    except:  # NOQA #noshame
        pass

print('Total Issues Created: {}'.format(issues_created))
print('Total Issues Assigned To: {}'.format(issues_assigned))
print('Total Repos Touched: {}'.format(len(repos)))
print('Total Commits Created: {}'.format(commits))
print('Total Lines Added: {}'.format(lines_added))
print('Total Lines Removed: {}'.format(lines_removed))
