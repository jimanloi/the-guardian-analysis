from datetime import date
import get_content
import visualisation
import quantitative_analyse
import nlp_analysis


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
    quantitative_analyse.count_articles_per_section_per_day(list_of_all_articles, list_section_count)
    print(list_section_count)
    date_section_counts = visualisation.parse_data(list_section_count)
    days, sections, y_values, section_totals = visualisation.prepare_data_for_stackplot(date_section_counts)
    visualisation.plot_stackplot(days, sections, y_values, section_totals)

top_keywords_opinion = nlp_analysis.extract_keywords_from_section(list_of_all_articles, "Opinion", 20)
print(f"Top Keywords for Opinion: {top_keywords_opinion}")
visualisation.save_wordcloud(top_keywords_opinion, "Opinion")
visualisation.plot_keywords(top_keywords_opinion, "Opinion")

#mention of a word in a section
"""
word_to_find = "harris"
number_of_mention = nlp_analysis.word_frequency_in_section(list_of_all_articles,"World news",word_to_find)
print(f"Frequency of the word {word_to_find}: {number_of_mention}")

top_keywords_world_news = nlp_analysis.extract_keywords_from_section(list_of_all_articles,"World news", 20)
print("Top Keywords for World News:", top_keywords_world_news)
visualisation.save_wordcloud(top_keywords_world_news, "World news")
visualisation.plot_keywords(top_keywords_world_news, "World news")

top_keywords_us_news = nlp_analysis.extract_keywords_from_section(list_of_all_articles, "US news", 20)
print("Top Keywords for US News:", top_keywords_us_news)
visualisation.save_wordcloud(top_keywords_us_news, "US news")
visualisation.plot_keywords(top_keywords_us_news, "US news")

"""


