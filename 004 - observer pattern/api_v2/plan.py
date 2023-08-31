from lib.db import create_user, find_user
from .event import post_event

def upgrade_plan(email: str):
    # find the user
    user = find_user(email)

    # upgrade the plan
    user.plan = "paid"

    # post an event
    post_event("user_upgrade_plan", user)