"""Exceptions"""


class FailedToPublish(Exception):
    """Failed To Publish Exception"""

    def __init__(self, msg='', data=None):
        self.msg = msg
        self.data = data

    def __str__(self):
        return f'{self.msg}: {self.data}'
