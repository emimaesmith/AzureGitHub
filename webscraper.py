import requests
import json

from github import get_issues, get_pull_requests

if __name__ == '__main__':

    # while True:
    # the_date = now()
    issues = get_issues()
    # pull_requests = get_pull_requests()
