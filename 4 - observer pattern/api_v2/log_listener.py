from lib.log import log
from .event import subscribe

def handle_user_registered_event(user):
    log(f"User registered with email address {user.email}")

def handle_user_password_forgotten_event(user):
    log(f"User with email address {user.email} requested a password reset")

def handle_user_upgrade_plan_event(user):
    log(f"User with email address {user.email} has upgraded their plan")

def setup_log_event_handlers():
    subscribe("user_registered", handle_user_registered_event)
    subscribe("user_password_forgotten", handle_user_password_forgotten_event)
    subscribe("user_upgrade_plan", handle_user_upgrade_plan_event)