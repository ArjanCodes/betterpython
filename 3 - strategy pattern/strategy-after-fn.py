import string
import random
from typing import List, Callable
from abc import ABC, abstractmethod


def generate_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


def fifoOrdering(list: List[SupportTicket]) -> List[SupportTicket]:
    return list.copy()


def filoOrdering(list: List[SupportTicket]) -> List[SupportTicket]:
    list_copy = list.copy()
    list_copy.reverse()
    return list_copy


def randomOrdering(list: List[SupportTicket]) -> List[SupportTicket]:
    list_copy = list.copy()
    random.shuffle(list_copy)
    return list_copy


def blackHoleOrdering(list: List[SupportTicket]) -> List[SupportTicket]:
    return []


class CustomerSupport:

    def __init__(self):
        self.tickets = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, ordering: Callable[[List[SupportTicket]], List[SupportTicket]]):
        # create the ordered list
        ticket_list = ordering(self.tickets)

        # if it's empty, don't do anything
        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done!")
            return

        # go through the tickets in the list
        for ticket in ticket_list:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")


# create the application
app = CustomerSupport()

# register a few tickets
app.create_ticket("John Smith", "My computer makes strange sounds!")
app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

# process the tickets
app.process_tickets(blackHoleOrdering)
