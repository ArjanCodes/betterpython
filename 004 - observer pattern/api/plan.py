from lib.email import send_email
from lib.db import create_user, find_user
from lib.log import log
from lib.slack import post_slack_message

def upgrade_plan(email: str):
    # find the user
    user = find_user(email)

    # upgrade the plan
    user.plan = "paid"

    # post a Slack message to sales department
    post_slack_message("sales",
        f"{user.name} has upgraded their plan.")

    # send a thank you email
    send_email(user.name, user.email,
        "Thank you",
        f"Thanks for upgrading, {user.name}! You're gonna love it. \nRegards, The DevNotes team")

    # write server log
    log(f"User with email address {user.email} has upgraded their plan")