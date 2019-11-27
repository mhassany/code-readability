from commits_helper import commits
from collections import defaultdict


def get_file_commits():
    """ yeild file name, count """
    # file => (add+del) count
    files = defaultdict(int)

    for commit in commits():
        for file in commit.files:
            files[file.name] += 1

    sorted_files = sorted(files.items(), key=lambda kv: kv[1], reverse=True)

    for file in sorted_files:
        # file name, count
        yield file


for commit in get_file_commits():
    print(commit)
