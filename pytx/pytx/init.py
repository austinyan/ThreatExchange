from errors import pytxInitError


__ACCESS_TOKEN__ = None


def init(app_id, app_secret):
    """
    Use the app_id and app_secret to store the access_token globally for all
    instantiated objects to leverage.

    :param app_id: The APP-ID to use.
    :type app_id: str
    :param app_secret: The APP-SECRET to use.
    :type app_secret: str
    :raises: :class:`errors.pytxIniterror`
    """

    global __ACCESS_TOKEN__
    try:
        __ACCESS_TOKEN__ = app_id + "|" + app_secret
    except Exception, e:
        raise pytxInitError("Error generating access token: %s" % str(e))
    return
