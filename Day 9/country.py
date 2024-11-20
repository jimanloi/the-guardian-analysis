

class Country:
    def __init__(self, continent, capital, population, head_of_government, currency):
        self.continent = continent
        self.capital = capital
        self.population = population
        self.head_of_government = head_of_government
        self.currency = currency

    def estimate_population_in_10years(self):
        if self.continent == "Europe":
            return self.population*1.15
        elif self.continent == "America":
            return self.population*1.2
        else:
            return self.population*1.4


if __name__ == "__main__":
    Belgium = Country("Europe","Brussels",11820000,"Alexander De Croo", "euro")
    United_Kingdom = Country("Europe","London",68350000,"Keir Starmer", "pound")
    France = Country("Europe","Paris",68170000,"Emmanuel Macron","euro")
    United_States = Country("America","Washington D.C.",334000000,"Joe Biden", "US dollar")


    print(f"The estimated population of belgium in 10 years is: {Belgium.estimate_population_in_10years():,.0f}.")



