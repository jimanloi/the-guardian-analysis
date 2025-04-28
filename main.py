import csv
from datetime import date, datetime, timedelta
from os.path import join, exists
import get_content
import visualisation
import quantitative_analyse
import nlp_analysis
from guardian import GuardianArticle



def main():
    folder_path = "guardian_articles"
    list_of_all_articles = []
    api_key = "e3574d33-be67-451d-bde6-ce32ffa11f78"
    api_endpoint = 'http://content.guardianapis.com/search'
    start_date = date(2024, 10, 1)
    end_date = date(2024, 10, 31)

    get_content.import_data_from_TheGuardian(api_key, api_endpoint, start_date, end_date, folder_path)
    get_content.get_readable_articles(list_of_all_articles, folder_path, GuardianArticle, start_date, end_date)

    # To see how many articles mention the word and save it to a csv
    word_to_find = "microsoft"
    output_file = f"articles_with_{word_to_find}.csv"
    nlp_analysis.find_articles_containing_a_word_to_csv(list_of_all_articles, word_to_find, output_file)

    # Frequency of a word in all articles
    section = "World news"
    number_of_mention = nlp_analysis.word_frequency_in_section(list_of_all_articles, section , word_to_find)
    print(f"Frequency of the word {word_to_find} in {section}: {number_of_mention}")

    """
    # To show no. of articles per section
    list_section_count = []
    quantitative_analyse.count_articles_per_section_per_day(list_of_all_articles, list_section_count)
    print(list_section_count)
    date_section_counts = visualisation.parse_data(list_section_count, start_date, end_date)
    days, sections, y_values, section_totals = visualisation.prepare_data_for_stackplot(date_section_counts)
    visualisation.plot_stackplot(days, sections, y_values, section_totals)

    top_keywords_opinion = nlp_analysis.extract_keywords_from_section(list_of_all_articles, "Opinion", 20)
    print(f"Top Keywords for Opinion: {top_keywords_opinion}")
    #visualisation.save_wordcloud(top_keywords_opinion, "Opinion")
    visualisation.plot_keywords(top_keywords_opinion, "Opinion")

    # To analysis the sentiment of articles in a section
    section_to_analyse = "Environment"
    output_file = f"sentiment_analysis_{section_to_analyse}.csv"
    sentiment_results = nlp_analysis.analyse_sentiment_by_section(list_of_all_articles, section_to_analyse)
    # nlp_analysis.export_sentiment_to_csv(sentiment_results, output_file)
    print(f"In the {section_to_analyse} section :")
    nlp_analysis.number_of_each_sentiment_label(sentiment_results, "Positive")
    nlp_analysis.number_of_each_sentiment_label(sentiment_results, "Negative")
    nlp_analysis.number_of_each_sentiment_label(sentiment_results, "Neutral")
    visualisation.visualise_sentiment_pie_chart(sentiment_results, section_to_analyse)
    
    number_of_mention = nlp_analysis.word_frequency_in_section(list_of_all_articles,"",word_to_find)
    print(f"Frequency of the word {word_to_find}: {number_of_mention}")
    
    #Find top keywords in a section
    
    top_keywords_opinion = nlp_analysis.extract_keywords_from_section(list_of_all_articles, "Opinion", 20)
    print(f"Top Keywords for Opinion: {top_keywords_opinion}")
    #visualisation.save_wordcloud(top_keywords_opinion, "Opinion")
    visualisation.plot_keywords(top_keywords_opinion, "Opinion")
    
    top_keywords_world_news = nlp_analysis.extract_keywords_from_section(list_of_all_articles,"World news", 20)
    print("Top Keywords for World News:", top_keywords_world_news)
    #visualisation.save_wordcloud(top_keywords_world_news, "World news")
    visualisation.plot_keywords(top_keywords_world_news, "World news")
    
    top_keywords_us_news = nlp_analysis.extract_keywords_from_section(list_of_all_articles, "US news", 20)
    print("Top Keywords for US News:", top_keywords_us_news)
    #visualisation.save_wordcloud(top_keywords_us_news, "US news")
    visualisation.plot_keywords(top_keywords_us_news, "US news")
    
    """

if __name__ == "__main__":
    main()