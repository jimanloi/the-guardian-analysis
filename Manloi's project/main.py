from datetime import date
import get_content


folder_path = "./tempdata/articles"
list_of_all_articles = []

class GuardianArticle:
    def __init__(self, article_data_from_json):
        self.type = article_data_from_json["type"]
        self.sectionName = article_data_from_json["sectionName"]
        self.webTitle = article_data_from_json["webTitle"]
        self.bodyText = article_data_from_json["fields"]["bodyText"]
        self.date = article_data_from_json.get("webPublicationDate")
        self.pillarName = article_data_from_json.get("pillarName")

    def __repr__(self):
        return (f"{self.type} in {self.sectionName} section : {self.webTitle} published at {self.date}")

    def get_bodytext(self):
        return self.bodyText


if __name__ == "__main__":
    api_key = "e3574d33-be67-451d-bde6-ce32ffa11f78"
    api_endpoint = 'http://content.guardianapis.com/search'
    params = {
        'from-date': "",
        'to-date': "",
        'order-by': "newest",
        'show-fields': 'all',
        'page-size': 200,
        'api-key': api_key
    }
    start_date = date(2024, 10, 1)
    end_date = date(2024, 10, 31)
    get_content.import_data_from_TheGuardian(api_key, api_endpoint, params, start_date, end_date)
    get_content.get_readable_articles(list_of_all_articles, folder_path, GuardianArticle)
    for article in list_of_all_articles:
        print(article)

# -Make a graph  - to show no.of articles per section
    list_section_count = []
    get_content.count_articles_per_section_per_day(list_of_all_articles, list_section_count)
    print(list_section_count)

date_section_counts = get_content.parse_data(list_section_count)
# Prepare the data for the stackplot
days, sections, y_values, section_totals = get_content.prepare_data_for_stackplot(date_section_counts)

# Plot the stackplot
get_content.plot_stackplot(days, sections, y_values, section_totals)