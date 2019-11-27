import requests
import logging
import json

logging.basicConfig(level=logging.DEBUG)

ISSUES_FOR_REPO_URL = 'https://api.github.com/repos/pallets/flask/issues?state=all'
AUTH = ("YOUR_GITHUB_USERNAME", "YOUR_GITHUB_PASSWORD")

# all_issues = []


def write_issues(r):
    if not r.status_code == 200:
        raise Exception(r.status_code)
    for issue in r.json():
        if issue['comments'] > 0:
            comments = get_comments(issue['comments_url'])
            issue['comments_inline'] = comments
        with open(str(issue["number"]) + ".json", "w") as issue_file:
            issue_file.write(json.dumps(issue, indent=4))
            issue_file.close()
    if 'link' in r.headers:
        pages = dict(
            [(rel[6:-1], url[url.index('<') + 1:-1]) for url, rel in
                [link.split(';') for link in
                    r.headers['link'].split(',')]])
        if 'next' in pages:
            write_issues(requests.get(pages['next'], auth=AUTH))


def get_comments(url):
    r = requests.get(url, auth=AUTH)
    if 'link' in r.headers:
        print('Paging not supported for comments download')
        return dict()
    else:
        return r.json()


write_issues(requests.get(ISSUES_FOR_REPO_URL, auth=AUTH))
