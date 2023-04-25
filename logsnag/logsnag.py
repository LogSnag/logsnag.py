""" LogSnag Client Implementation """
import requests
from logsnag.constants import ENDPOINTS
from logsnag.exceptions import FailedToPublish
from logsnag.utils import create_authorization_header
from typing import Optional, Union
from datetime import datetime


class LogSnag:
    """LogSnag API Client"""

    def __init__(self, token: str, project: str, disable_tracking: bool = False):
        """
        Initialize a new instance of LogSnag
        :param token: API Token
        :param project: Project name
        :param disable_tracking: disable tracking
        """
        self._token = token
        self._project = project
        self._disabled = disable_tracking
        self._setup_request_session()

        self.insight = self._Insight(self)

    def _setup_request_session(self):
        """Set up a new Instance of Requests' Session"""
        session = requests.Session()
        session.headers.update({'Content-Type': 'application/json'})
        session.headers.update(create_authorization_header(self._token))
        self._session = session

    def get_project(self):
        """Get project name"""
        return self._project

    def disable_tracking(self):
        """Disable tracking"""
        self._disabled = True

    def enable_tracking(self):
        """Enable tracking"""
        self._disabled = False

    def is_disabled(self):
        """Check if tracking is disabled"""
        return self._disabled

    def get_session(self):
        """Get the current session"""
        return self._session

    def track(
            self,
            channel: str,
            event: str,
            user_id: Optional[str] = None,
            description: Optional[str] = None,
            icon: Optional[str] = None,
            tags: Optional[dict] = None,
            notify: Optional[bool] = None,
            parser: Optional[str] = None,
            date: Optional[datetime] = None,
    ):
        """
        Publish a new log to LogSnag
        :param channel: channel name
        :param event: event title
        :param user_id: optional user id
        :param description: optional event description
        :param icon: optional event icon (must be a single emoji)
        :param tags: optional dictionary of tags
        :param notify: notifies via push notifications
        :param parser: optional parser for description (markdown or text)
        :param date: optional datetime for historical logs
        :raises:
            FailedToPublish: if failed to publish
        """

        if self._disabled:
            return

        timestamp = None
        if date:
            # convert timestamp to unix timestamp
            timestamp = date.timestamp()

        data = {
            "project": self.get_project(),
            "channel": channel,
            "user_id": user_id,
            "event": event,
            "description": description,
            "icon": icon,
            "tags": tags,
            "notify": notify,
            "parser": parser,
            "timestamp": timestamp
        }

        # drop none values from json body
        data = {k: v for k, v in data.items() if v is not None}
        response = self._session.post(ENDPOINTS.LOG, json=data)

        if not 200 <= response.status_code < 300:
            raise FailedToPublish()

    def identify(
            self,
            user_id: str,
            properties: dict,
    ):
        """
        Identify a user
        :param user_id: user id
        :param properties: user properties
        :raises:
            FailedToPublish: if failed to publish
        """

        if self.is_disabled():
            return

        data = {
            "project": self.get_project(),
            "user_id": user_id,
            "properties": properties
        }

        response = self._session.post(ENDPOINTS.IDENTIFY, json=data)

        if not 200 <= response.status_code < 300:
            raise FailedToPublish()

    class _Insight:

        def __init__(self, logsnag):
            self._logsnag = logsnag

        def track(
                self,
                title: str,
                value: Union[int, float, str],
                icon: Optional[str] = None,
        ):
            """
            Publish a new insight to LogSnag
            :param title: insight title
            :param value: insight value
            :param icon: optional event icon (must be a single emoji)
            :raises:
                FailedToPublish: if failed to publish
            """

            if self._logsnag.is_disabled():
                return

            data = {
                "project": self._logsnag.get_project(),
                "title": title,
                "value": value,
                "icon": icon
            }

            # drop none values from json body
            data = {k: v for k, v in data.items() if v is not None}
            response = self._logsnag.get_session().post(ENDPOINTS.INSIGHT, json=data)

            if not 200 <= response.status_code < 300:
                raise FailedToPublish()

        def increment(
                self,
                title: str,
                value: Union[int, float],
                icon: Optional[str] = None,
        ):
            """
            Increment an existing insight
            :param title: insight title
            :param value: increment value
            :param icon: optional event icon (must be a single emoji)
            :raises:
                FailedToPublish: if failed to publish
            """

            if self._logsnag.is_disabled():
                return

            data = {
                "project": self._logsnag.get_project(),
                "title": title,
                "value": {
                    "$inc": value
                },
                "icon": icon
            }

            # drop none values from json body
            data = {k: v for k, v in data.items() if v is not None}
            response = self._logsnag.get_session().patch(ENDPOINTS.INSIGHT, json=data)

            if not 200 <= response.status_code < 300:
                raise FailedToPublish()
