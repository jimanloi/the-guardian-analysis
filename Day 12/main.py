import csv

class World_happiness_report:
    def __init__(self, _name:str, _region:str, _year, _life_ladder, _gdp_per_capita, _social_support, _healthy_life_expectancy_at_birth, _freedom_to_make_life_choices, _generosity, _perceptions_of_corruption, _confidence_in_national_government):
        self.name = _name
        self.region = _region
        self.year = _year
        self.life_ladder = _life_ladder
        self.gdp_per_capita = _gdp_per_capita
        self.social_support = _social_support
        self.healthy_life_expectancy_at_birth = _healthy_life_expectancy_at_birth
        self.freedom = _freedom_to_make_life_choices
        self.generosity = _generosity
        self.perceptions_of_corruption = _perceptions_of_corruption
        self.confidence_in_national_government = _confidence_in_national_government


whrs = []

with (open('World Happiness Report(1).csv', newline='') as csvfile):
    reader_whr = csv.reader(csvfile, delimiter=',')
    next(reader_whr)
    for row in reader_whr:
        stat1 = World_happiness_report(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],row[8], row[9],row[12])
        whrs.append(stat1)
print(whrs[0].name)

#to calculate the average generosity in the world
counter = 0
sum_of_generosity = 0.0
for whr in whrs:
    if (whr.generosity != "" ""):
        counter += 1
        sum_of_generosity += float(whr.generosity)
print(sum_of_generosity/counter)

#to calculate the average life expectancy in Belgium
sum_of_life_expectancy_belgium = 0
counter = 0
for whr in whrs:
    if whr.healthy_life_expectancy_at_birth != "" "" and whr.name == "New Zealand":
        counter += 1
        sum_of_life_expectancy_belgium += float(whr.healthy_life_expectancy_at_birth)
print(sum_of_life_expectancy_belgium/counter)

#to find out the country with the most social support
greatest_social_support = whrs[0].social_support
country_with_best_social_support = whrs[0].name
for whr in whrs:
    if whr.social_support!=' ' and whr.social_support > greatest_social_support:
        greatest_social_support = whr.social_support
        country_with_best_social_support = whr.name
print(country_with_best_social_support+' '+greatest_social_support)

#find out in which country we feel the least free
min = whrs[0].freedom
least_free_country = whrs[0].name
for whr in whrs:
    if whr.freedom != " ":
        if whr.freedom < min :
            min = whr.freedom
            least_free_country = whr.name
print(least_free_country)

