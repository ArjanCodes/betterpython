#!/usr/bin/env python3


class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class SMSAuth:

    def __init__(self):
        self.authorized = False

    def verify_code(self, code):
        print(f'Verifying SMS code {code!r}')
        self.authorized = True


class GoogleAuth:

    def __init__(self):
        self.authorized = False

    def verify_code(self, code):
        print(f'Verifying GoogleAuth code {code!r}')
        self.authorized = True


class NotARobotAuth:

    def __init__(self):
        self.authorized = False

    def not_a_robot(self):
        self.authorized = True


class DebitPaymentProcessor:

    def __init__(self, security_code, authorizer):
        self.security_code = security_code
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.authorized:
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor:

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor:

    def __init__(self, email_address, authorizer):
        self.email_address = email_address
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.authorized:
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Using email address: {self.email_address}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
authorizer = GoogleAuth()
authorizer.verify_code(9445)
processor = PaypalPaymentProcessor("hi@arjancodes.com", authorizer)
processor.pay(order)
