from api_v2.slack_listener import setup_slack_event_handlers
from api_v2.log_listener import setup_log_event_handlers
from api_v2.email_listener import setup_email_event_handlers

from api_v2.user import register_new_user, password_forgotten
from api_v2.plan import upgrade_plan

# initialize the event structure
setup_slack_event_handlers()
setup_log_event_handlers()
setup_email_event_handlers()


# register a new user
register_new_user("Arjan", "BestPasswordEva", "hi@arjanegges.com")

# send a password reset message
password_forgotten("hi@arjanegges.com")

# upgrade the plan
upgrade_plan("hi@arjanegges.com")
