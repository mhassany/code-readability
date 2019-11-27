from commits_helper import commits
from collections import namedtuple, defaultdict


def get_file_contributors(file_name):
    """ yeild contributor, change count, changes date """
    # -- sorted contributors by number of commits(changes)
    contributors = defaultdict(int)
    contributed_at = defaultdict(list)

    for commit in commits():
        for file in commit.files:
            if file.name == file_name:
                contributors[commit.author] += 1
                contributed_at[commit.author].append(commit.date)

    sorted_contributors = sorted(
        contributors.items(), key=lambda kv: kv[1], reverse=True)

    for contributor in sorted_contributors:
        # contributor, change count, changes date
        yield contributor[0], contributor[1], contributed_at[contributor[0]]


for contributor in get_file_contributors("flask/app.py"):
    print(contributor)
