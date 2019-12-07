from issues_helper import issues, get_only_texts, get_only_words
from collections import Counter, defaultdict


# list of files in pallets/flask repo
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


# count the number of times each file is mentioned in an issue or comment
def issues_by_files():
    # for each issue
    for issue in issues():
        # for each file
        for file in files:
            # count them
            count = 0
            count += issue["title"].count(file)

            if "body" in issue.keys() and issue["body"]:
                count += issue["body"].count(file)

            if "comments_inline" in issue.keys():
                for comment in issue["comments_inline"]:
                    count += comment["body"].count(file)

            if count != 0:
                yield file, issue


# return a single text containing all the 
# readable texts in an issue
def get_issue_texts(issue):
    text = ""
    text += " " + issue["title"]
    if issue["body"]:
        text += " " + issue["body"]

    if "comments_inline" in issue:
        for comment in issue["comments_inline"]:
            text += " " + comment["body"]

    return text


# our negative keywords
nagative_words = [
    "hard to read", "hard to debug", "hard to understand", "hard to spot", "hard to remember",
    "harder to read", "harder to debug", "harder to understand", "harder to spot", "harder to remember",
    "not readable", "readability",
    "not understandable", "understandability",
    "comprehension", "comprehend", "not comprehensible",
    "confuse", "confusing", "confusion",
    "clean up", "cleanup",
    "indentation", "indent level",

    "formatting", "variable name", "line length",
    "line break", "order of code", "ambiguous names", "clear name",
    "duplicate", "duplication",
    "unused code", "complex code", "complicated",
    # some keywords are too general
    "order of line",
    # some can means too many other things
    # ignore this=>"bad code", "bad piece of code",
    "bad comment",
    "clarify", "clarified", "clarification",
    "misleading", "is vague", "is too vague",
    "bad name", "bad naming", "bad names",
    "not meaningful", "not descriptive",

    "typo", "long name", "short name",
    "redundant comment", "redundant code",
    "rename", "renaming"
]


# count the negative words in the issue
def count_words():
    file_hit = defaultdict(int)

    # file, issue
    for file, issue in issues_by_files():
        texts = get_issue_texts(issue)

        count = 0
        for neg_word in nagative_words:
            count += texts.count(neg_word)

        file_hit[file] += count

    for file, hit in file_hit.items():
        yield file, hit


for file, hit in count_words():
    print(hit, file)
