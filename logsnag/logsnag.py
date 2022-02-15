""" LogSnag Client Implementation """
import requests
from logsnag.constants import LOGSNAG_ENDPOINT
from logsnag.exceptions import FailedToPublish
from logsnag.utils import create_authorization_header


class LogSnag:
    """LogSnag API Client"""

    def __init__(self, token: str):
        """
        Initialize a new instance of LogSnag
        :param token: API Token
        """
        self._token = token
        self._setup_request_session()

    def _setup_request_session(self):
        """Set up a new Instance of Requests' Session"""
        session = requests.Session()
        session.headers.update({'Content-Type': 'application/json'})
        session.headers.update(create_authorization_header(self._token))
        self._session = session

    def publish(
            self,
            project: str,
            channel: str,
            event: str,
            description: str = None,
            icon: str = None,
            notify: bool = False
    ):
        """
        Publish a new log to LogSnag
        :param project: project name
        :param channel: channel name
        :param event: event title
        :param description: optional event description
        :param icon: optional event icon (must be a single emoji)
        :param notify: notify via push notifications
        """
        response = self._session.post(LOGSNAG_ENDPOINT, json={
            "project": project,
            "channel": channel,
            "event": event,
            "description": description,
            "icon": icon,
            "notify": notify
        })

        if not 200 <= response.status_code < 300:
            raise FailedToPublish()
