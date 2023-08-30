"""Utility functions"""


def create_authorization_header(token: str):
    """
    Generate authorization header for LogSnag
    :param token: API Token
    :return: Authorization Header
    """
    return {"Authorization": f"Bearer {token}"}
