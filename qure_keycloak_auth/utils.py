from user_agents import parse as ua_parser
from app_settings import AUTH_SESSION_COOKIE_AGE, AUTH_SESSION_COOKIE_AGE_MOBILE


def set_session_expiry(request):
    # set session expiry based on device
    ua = ua_parser(request.axes_user_agent)
    if ua.is_mobile:
        session_expiry = AUTH_SESSION_COOKIE_AGE_MOBILE
    else:
        session_expiry = AUTH_SESSION_COOKIE_AGE
    request.session.set_expiry(session_expiry)
    request.session["ua"] = request.axes_user_agent
