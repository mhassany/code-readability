from issues_helper import issues, get_only_texts, get_only_words
from collections import Counter, defaultdict


def get_issue_words():
    words = list()

    for issue in get_only_words():
        for i in range(len(issue.words) - 3):
            words.append(" ".join(issue.words[i:i + 3]))

    top_most = Counter(words).most_common()
    for word in top_most:
        if word[1] > 10:
            print(word[1], word[0])


def get_issue_labels():
    labels = list()

    for issue in get_only_words():
        labels.extend(issue.labels)

    return dict(Counter(labels))


# print(get_issue_labels())
# get_issue_words()

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


def issues_by_files():
    for issue in issues():
        for file in files:
            count = 0
            count += issue["title"].count(file)

            if "body" in issue.keys() and issue["body"]:
                count += issue["body"].count(file)

            if "comments_inline" in issue.keys():
                for comment in issue["comments_inline"]:
                    count += comment["body"].count(file)

            if count != 0:
                yield file, issue


def issues_by_file_labels(label):
    for file, issue in issues_by_files():
        if "labels" in issue and label in [label["name"] for label in issue["labels"]]:
            yield file, issue


def look_files_hits_in_issues():
    file_hits = defaultdict(int)
    file_labels = defaultdict(lambda: defaultdict())

    for issue in issues():
        for file in files:
            count = 0
            count += issue["title"].count(file)

            if "body" in issue.keys() and issue["body"]:
                count += issue["body"].count(file)

            if "comments_inline" in issue.keys():
                for comment in issue["comments_inline"]:
                    count += comment["body"].count(file)

            file_hits[file] += count

            if count != 0 and "labels" in issue:
                labels = issue["labels"]

                file_labels[file].extend([label["name"] for label in labels])

    for file, hit in file_hits.items():
        print(file, hit, file_labels[file])


# look_files_hits_in_issues()

def get_issue_texts(issue):
    text = ""
    text += " " + issue["title"]
    if issue["body"]:
        text += " " + issue["body"]

    if "comments_inline" in issue:
        for comment in issue["comments_inline"]:
            text += " " + comment["body"]

    return text


def __test():
    # "blocker", "bug",
    #
    # "discussion", "docs", "question"
    for label in [
        "blocker", "bug"
        #
        "discussion", "docs", "question"
    ]:
        print("----------------------------------------")
        print("Label:", label)
        print()

        for file, issue in issues_by_file_labels('bug'):
            print("\tFile: ", file)
            print("\tIssue: ", issue["title"])
            text = get_issue_texts(issue)
            print("\t", text.count("spacing"))
            print()


def list_phrase():
    phrases = list()

    for issue in issues():
        words = get_issue_texts(issue).split(" ")

        for i in range(len(words) - 3):
            phrases.append(" ".join(words[i:i + 3]))

    grouped = Counter(phrases).most_common()

    for each in grouped:
        print(each)


list_phrase()
