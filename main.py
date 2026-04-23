# Завдання 1


class CreditCardPayment:
    def __init__(self, currency):
        self._currency = currency

    def pay(self, amount):
        print(f"Оплата карткою {amount}{self._currency}")


class PayPalPayment:
    def __init__(self, currency):
        self._currency = currency

    def pay(self, amount):
        print(f"Оплата PayPal {amount}{self._currency}")


class CryptoPayment:
    def __init__(self, currency):
        self._currency = currency

    def pay(self, amount):
        print(f"Оплата криптогаманцем {amount}{self._currency}")


def create_payment():
    payment_type = input("Введіть тип платежу (card / paypal / crypto): ").lower()
    currency = input("Введіть валюту: ")

    if payment_type == "card":
        return CreditCardPayment(currency)

    elif payment_type == "paypal":
        return PayPalPayment(currency)

    elif payment_type == "crypto":
        return CryptoPayment(currency)

    else:
        print("Невідомий тип!")
        return None


payments = []

for _ in range(3):
    p = create_payment()
    if p:
        payments.append(p)


for p in payments:
    amount = float(input("Введіть суму: "))
    p.pay(amount)
