#program a currency converter

class Currency:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
        self.value_to_eur = {"EUR":1, "USD":0.95,"GBP":1.2, "CAD":0.67, "JPY":0.0061, "INR":0.011}

    def set_amount(self, new_amount):
        self.amount = new_amount

    def get_euro(self):
        return self.amount*self.value_to_eur[self.currency]

    def convert_to(self, new_currency):
        target_rate = self.value_to_eur[new_currency]
        return self.get_euro() / target_rate


if __name__ == "__main__":
    euro = Currency(100, "EUR")
    usd = Currency(100, "USD")
    gbp = Currency(100, "GBP")
    cad = Currency(100,"CAD")
    jpy = Currency(6000,"JPY")
    inr = Currency(100,"INR")

    print(f"USD10 = GBP{usd.convert_to('GBP'):.2f}")