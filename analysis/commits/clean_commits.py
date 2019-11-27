# git log --stat=100000 > ../../code-readability/analysis/commits/commits.txt

import re
from collections import namedtuple, defaultdict


def __token(commit, i_str, e_str, default):
    _i = commit.find(i_str)

    if _i >= 0:
        _i += len(i_str)
        _e = commit.find(e_str, _i)
        return commit[_e:], commit[_i: _e].strip()
    else:
        return commit, default


def parse(commit):
    commit, commit_id = __token(commit, "commit ", "\n", None)  # find the id
    commit, merge_id = __token(commit, "Merge: ", "\n", None)  # find the merge
    commit, author = __token(commit, "Author: ", "\n", None)  # find the author
    commit, date = __token(commit, "Date: ", "\n", None)  # find the date
    commit, comment = __token(commit, "\n\n", "\n\n", None)  # find the comment

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
            yield parse(commit)
            commit = line
        else:
            commit += line


def print_list():
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


def aggregate_changes():
    # TODO aggreate file changes to generate lists and graphs
    ""
    # -- sorted file by number of time changed
    files = defaultdict(int)

    for commit in commits():
        for file in commit.files:
            files[file.name] += 1

    sorted_files = sorted(files.items(), key=lambda kv: kv[1], reverse=True)

    for file in sorted_files:
        print(file[1], file[0])


aggregate_changes()
