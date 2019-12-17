import os
import json
from collections import namedtuple, Counter


# return the issues one by one
def issues():
    # for now there are 3438 issues
    for number in range(1, 3439):
        path = "./issues/" + str(number) + ".json"

        if os.path.exists(path):
            file = open(path, "r")
            issue = json.load(file)
            file.close()
            yield issue


# only return the title,body,labels,comment.body
def get_only_texts():
    for issue in issues():
        title = issue["title"]
        body = issue["body"]
        user = issue["user"]["login"]
        labels = [label["name"] for label in issue["labels"]]

        comments = list()
        Comment = namedtuple("Comment", ["user", "body"])
        if "comments_inline" in issue:
            for comment in issue["comments_inline"]:
                comments.append(
                    Comment(comment["user"]["login"], comment["body"]))

        Issue = namedtuple(
            "Issue", ["user", "title", "body", "labels", "comments"])
        yield Issue(user, title, body, labels, comments)


# break the issues texts into words
def get_only_words():
    for issue in get_only_texts():
        words = list()
        if issue.title:
            words.extend(issue.title.lower().split(" "))
        if issue.body:
            words.extend(issue.body.lower().split(" "))
        for comment in issue.comments:
            words.extend(comment.body.lower().split(" "))

        Issue = namedtuple(
            "Issue", ["labels", "words"])
        yield Issue(issue.labels, words)
