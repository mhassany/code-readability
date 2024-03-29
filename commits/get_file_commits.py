from commits_helper import commits
from collections import defaultdict


def get_file_line_changes():
    """ yeild file name, line_added, line_removed """
    # file => (add+del) count
    line_changes = defaultdict(int)
    line_added = defaultdict(int)
    line_removed = defaultdict(int)

    for commit in commits():
        for file in commit.files:
            line_added[file.name] += file.line_added
            line_removed[file.name] += file.line_removed
            line_changes[file.name] += file.line_added + file.line_removed

    sorted_files = sorted(line_changes.items(),
                          key=lambda kv: kv[1], reverse=True)

    for file in sorted_files:
        # name, line_added, line_removed
        yield file[0], line_added[file[0]], line_removed[file[0]]


for line_change in get_file_line_changes():
    print(line_change)
