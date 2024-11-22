from datetime import date
import get_content
from collections import defaultdict

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

    def count_articles_by_section(articles_list):
        """Count the number of articles in each section."""
        section_counts = defaultdict(int)
        for article in list_of_all_articles:
            if article.sectionName:  # Ensure there's a sectionId
                section_counts[article.sectionName] += 1
        return section_counts


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

    section_counts = GuardianArticle.count_articles_by_section(list_of_all_articles)
    # Print the results
    print("Article count per section:")
    for section, count in section_counts.items():
        print(f"Section: {section}, Article Count: {count}")



