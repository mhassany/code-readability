# git log --stat=100000 > ../../code-readability/analysis/commits/commits.txt

import re
from collections import namedtuple, defaultdict


def __substr(commit, i_str, e_str, default):
    _i = commit.find(i_str)

    if _i >= 0:
        _i += len(i_str)
        _e = commit.find(e_str, _i)
        return commit[_e:], commit[_i: _e].strip()
    else:
        return commit, default


def parse_commit(commit):
    commit, commit_id = __substr(commit, "commit ", "\n", None)  # find the id
    commit, merge_id = __substr(commit, "Merge: ", "\n", None)  # find the merge
    commit, author = __substr(commit, "Author: ", "\n", None)  # find the author
    commit, date = __substr(commit, "Date: ", "\n", None)  # find the date
    commit, comment = __substr(commit, "\n\n", "\n\n", None)  # find the comment

    # find the summary
    change_summary = list(re.finditer(
        "\d+ files? changed(, \d+ insertions?\(\+\))?(, \d+ deletions?\(\-\))?", commit))

    # -- will be used to find the files
    summary_i = None
    if len(change_summary) > 0:
        summary_i = change_summary[0].span()[0]

    f_stats = list()
    if summary_i:
        files = commit[0:summary_i].strip()
        for file in files.split("\n"):
            file = file.strip()
            sep = file.find(" | ")

            file_name = file[0:sep].strip()
            is_binary = False
            line_added = None
            line_removed = None

            summary = file[sep + 3:]
            if summary.startswith("Bin "):
                is_binary = True
            else:
                line_added = summary.count("+")
                line_removed = summary.count("-")

            File = namedtuple('File', ['name', 'is_binary',
                                       'line_added', 'line_removed'])
            f_stats.append(
                File(file_name, is_binary, line_added, line_removed))

    Commit = namedtuple('Commit', ['commit', 'merge', 'author',
                                   'date', 'comment', 'files'])
    return Commit(commit_id, merge_id, author, date, comment, f_stats)


def commits():
    all_commits = open("./commits.txt", "r")

    commit = ""

    for line in all_commits:
        if line.startswith("commit ") and len(commit) > 0:
            yield parse_commit(commit)
            commit = line
        else:
            commit += line


def print_commits_list():
    for commit in commits():
        print("\tCommit:", commit.commit)
        print("\tMerge:", commit.merge)
        print("\tAuthor:", commit.author)
        print("\tDate:", commit.date)

        if len(commit.files) != 0:
            print()
            print("\t\t{:>3} {:>3}   {:100}".format("+", "-", "file_name"))
            print("\t\t" + ("-" * 50))
            for file in commit.files:
                if file.is_binary:
                    print("\t\t{:>7}   {:100}".format("BINARY", file.name))
                else:
                    print("\t\t{:3d} {:3d}   {:100}".format(
                        file.line_added, file.line_removed, file.name))

        print()
        print()
        print()


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


for l in get_file_contributors("flask/app.py"):
    print(l)
