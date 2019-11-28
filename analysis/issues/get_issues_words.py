from issues_helper import issues, get_only_texts, get_only_words
from collections import Counter, Counter


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
get_issue_words()
