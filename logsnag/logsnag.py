""" LogSnag Client Implementation """
import requests
from logsnag.constants import ENDPOINTS
from logsnag.exceptions import FailedToPublish
from logsnag.utils import create_authorization_header
from typing import Union


class LogSnag:
    """LogSnag API Client"""

    def __init__(self, token: str, project: str):
        """
        Initialize a new instance of LogSnag
        :param token: API Token
        :param project: Project name
        """
        self._token = token
        self._project = project
        self._setup_request_session()

    def _setup_request_session(self):
        """Set up a new Instance of Requests' Session"""
        session = requests.Session()
        session.headers.update({'Content-Type': 'application/json'})
        session.headers.update(create_authorization_header(self._token))
        self._session = session

    def get_project(self):
        """Get project name"""
        return self._project

    def publish(
            self,
            channel: str,
            event: str,
            description: str = None,
            icon: str = None,
            tags: dict = None,
            notify: bool = False,
            parser: str = None
    ):
        """
        Publish a new log to LogSnag
        :param channel: channel name
        :param event: event title
        :param description: optional event description
        :param icon: optional event icon (must be a single emoji)
        :param tags: optional dictionary of tags
        :param notify: notify via push notifications
        :param parser: optional parser for description (markdown or text)
        :raises:
            FailedToPublish: if failed to publish
        """

        data = {
            "project": self.get_project(),
            "channel": channel,
            "event": event,
            "description": description,
            "icon": icon,
            "tags": tags,
            "notify": notify,
            "parser": parser
        }

        # drop none values from json body
        data = {k: v for k, v in data.items() if v is not None}
        response = self._session.post(ENDPOINTS.LOG, json=data)

        if not 200 <= response.status_code < 300:
            raise FailedToPublish()

    def insight(
            self,
            title: str,
            value: Union[int, float, str],
            icon: str = None,
    ):
        """
        Publish a new insight to LogSnag
        :param title: insight title
        :param value: insight value
        :param icon: optional event icon (must be a single emoji)
        :raises:
            FailedToPublish: if failed to publish
        """

        data = {
            "project": self.get_project(),
            "title": title,
            "value": value,
            "icon": icon
        }

        # drop none values from json body
        data = {k: v for k, v in data.items() if v is not None}
        response = self._session.post(ENDPOINTS.INSIGHT, json=data)

        if not 200 <= response.status_code < 300:
            print(response.text)
            raise FailedToPublish()
