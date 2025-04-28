#program a currency converter

class Currency:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
        self._value_to_eur = {"EUR":1.0, "USD":0.95,"GBP":1.2, "CAD":0.67, "JPY":0.0061, "INR":0.011}
        if self.currency not in self._value_to_eur:
            print("Currency not found")

    def set_amount(self, new_amount):
        self.amount = new_amount

    def get_euro(self):
        return self.amount*self._value_to_eur[self.currency]

    def convert_to(self, new_currency):
        return self.get_euro() / self._value_to_eur[new_currency]


if __name__ == "__main__":
    wallet1 = Currency(100, "EUR")
    print(f"{wallet1.currency}{wallet1.amount} = JPY{wallet1.convert_to('JPY'):.2f}")       #EUR to JPY

    wallet2 = Currency(100, "USD")
    print(f"{wallet2.currency}{wallet2.amount} = GBP{wallet2.convert_to('GBP'):.2f}")       #USD to GBP


