import requests
import json

from github_issue import GitHubIssue

def get_issues(org='ngageoint', repo='scale', end_date=None):
    """Returns the issues JSON for the specified org/repo

    {
        "url": "https://api.github.com/repos/ngageoint/seed-cli/issues/62",
        "repository_url": "https://api.github.com/repos/ngageoint/seed-cli",
        "labels_url": "https://api.github.com/repos/ngageoint/seed-cli/issues/62/labels{/name}",
        "comments_url": "https://api.github.com/repos/ngageoint/seed-cli/issues/62/comments",
        "events_url": "https://api.github.com/repos/ngageoint/seed-cli/issues/62/events",
        "html_url": "https://github.com/ngageoint/seed-cli/issues/62",
        "id": 248411986,
        "node_id": "MDU6SXNzdWUyNDg0MTE5ODY=",
        "number": 62,
        "title": "Identify issues and technologies for standalone Seed CLI",
        "labels": [
              {
                    "id": 976187133,
                    "node_id": "MDU6TGFiZWw5NzYxODcxMzM=",
                    "url": "https://api.github.com/repos/ngageoint/seed-cli/labels/on%20hold",
                    "name": "on hold",
                    "color": "ed0264",
                    "default": false,
                    "description": "issues being deferred for later"
              }
        ],
        "state": "open",
        "locked": false,
        "assignee": null,
        "assignees": [],
        "milestone": null,
        "comments": 0,
        "created_at": "2017-08-07T13:30:49Z",
        "updated_at": "2018-06-26T18:29:49Z",
        "closed_at": null,
        "author_association": "CONTRIBUTOR",
        "body": "Currently the Seed CLI requires a local installation of the Docker engine and CLI. This simplifies things, but requires more domain expertise on the part of the user. If we can get away from this requirement with minimal effort, we should do so.\r\n\r\nWe need to investigate the basic technologies available to us and come up with a reasonable recommendation for moving away from requiring Docker daemon running on host system. Seed CLI should support standalone build / execution of Seed images using technology such as libcontainer, etc.\r\n\r\nI anticipate some likely stumbling blocks:\r\n\r\n* Requirement to support registry auth\r\n* Management of Docker image layers\r\n* Parsing of Dockerfile statements for build\r\n\r\nIf any of these are determined as too big of a development effort, we need to know before we dive in."
    }

    :param org: The organization to search for
    :param repo: The repository name to search for
    :return: JSON list of issues
    """

    # Grabs all issues
    url = 'https://api.github.com/repos/%s/%s/issues?state=all' % (org, repo)
    response = requests.get(url)
    if end_date:
        url = '%s?since=%s' % (url, end_date)
    if response.status_code != 200:
        print('%d response when getting issues' % response.status_code)
        return

    json_issues = json.loads(response.content)
    print(len(json_issues))
    issues = []
    for issue in json_issues:
        issues.append(GitHubIssue(issue))
    # import pdb; pdb.set_trace()
    print(len(issues))


def get_pull_requests(org='ngageoint', repo='scale', end_date=None):
    resp = requests.get('https://api.github.com/repos/%s/%s/pulls' % (org, repo))
    if resp.status_code == 200:
        result = json.loads(resp.content)

        print('API response: ', resp.content)

