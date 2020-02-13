
class GitHubIssue(object):

    def __init__(self, issue_dict):

        if not issue_dict:
            return

        if 'url' in issue_dict:
            self._url = issue_dict['url']

        if 'repository_url' in issue_dict:
            self._repository_url = issue_dict['repository_url']

        if 'labels_url' in issue_dict:
            self._labels_url = issue_dict['labels_url']

        if 'comments_url' in issue_dict:
            self._comments_url = issue_dict['comments_url']

        if 'events_url' in issue_dict:
            self._events_url = issue_dict['events_url']

        if 'html_url' in issue_dict:
            self._html_url = issue_dict['html_url']

        if 'number' in issue_dict:
            self._issue_number = issue_dict['number']

        if 'labels' in issue_dict:
            self._labels = []
            for label in issue_dict['labels']:
                self._labels.append(label['name'])

        if 'state' in issue_dict:
            self._state = issue_dict['state']

        if 'assignee' in issue_dict:
            self._assignee = issue_dict['assignee']

        if 'created_at' in issue_dict:
            self._created_date = issue_dict['created_at']

        if 'updated_at' in issue_dict:
            self._last_updated = issue_dict['updated_at']

        if 'title' in issue_dict:
            self._issue_title = issue_dict['title']

        if 'body' in issue_dict:
            self._description = issue_dict['body']

    def to_json(self):
        """Returns the GitHub issue as JSON"""

        issue_dict = {}
        if self._url:
            issue_dict['usl'] = self._url

        if self._repository_url:
            issue_dict['repository_url'] = self._repository_url

        if self._labels_url:
            issue_dict['labels_url'] = self._labels_url

        if self._comments_url:
            issue_dict['comments_url'] = self._comments_url

        if self._events_url:
            issue_dict['events_url'] = self._events_url

        if self._html_url:
            issue_dict['html_url'] = self._html_url

        # if 'labels' in issue_dict:
        #     self._labels = []
        #     for label in issue_dict['labels']:
        #         self._labels.append(label['name'])

        if self._state:
            issue_dict['state'] = self._state

        if self._assignee:
            issue_dict['assignee'] = self._assignee

        if self._created_date:
            issue_dict['created_at'] = self._created_date

        if self._last_updated:
            issue_dict['updated_at'] = self._last_updated

        if self._issue_number:
            issue_dict['number'] = self._issue_number

        if self._issue_title:
            issue_dict['title'] = self._issue_title

        if self._description:
            issue_dict['body'] = self._description
