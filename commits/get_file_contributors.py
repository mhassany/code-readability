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


files = [
    "flask/app.py",
    "flask/cli.py",
    "flask/helpers.py",
    "flask/sessions.py",
    "flask/wrappers.py",
    "flask/blueprints.py",
    "flask/ctx.py",
    "flask/testing.py",
    "flask/module.py",
    "flask/json/tag.py",
    "flask/templating.py",
    "flask/run.py",
    "flask/__init__.py",
    "flask/json.py",
    "flask/config.py",
    "flask/debughelpers.py",
    "flask/_compat.py",
    "flask/logging.py",
    "flask/json/__init__.py",
    "flask/exthook.py",
    "flask/views.py",
    "flask/ext/__init__.py",
    "flask/signals.py",
    "flask/conf.py",
    "flask/globals.py",
    "flask/session.py",
    "flask/exceptions.py",
    "flask/__main__.py",
]

for file in files:
    print(file, len(list(get_file_contributors(file))))
