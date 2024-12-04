import os
from sys import excepthook

import spacy
import nltk
from nltk.corpus import stopwords, words
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('vader_lexicon')
from collections import Counter
import csv
from datetime import datetime

nlp = spacy.load("en_core_web_sm")

custom_stopwords = {'said', 'us', 'would', 'also', 'one', 'two', 'three', 'could', 'will', 'did', 'and', 'the', 'in',
                    'of', 'to', 'a', 'for', 'on', 'at', 'go','tell', 'find', 'say', 'take','year','day','get','come',
                    'make','new','time','last','include','call','like','see','first','week','know','since','many','use',
                    'well','even','way','long','much','want','back','may'}


# Text preprocessing: Remove unwanted characters
def preprocess_text(text):
    if isinstance(text, list):  # Join lists into a single string
        text = " ".join(text)
    words = word_tokenize(text.lower())
#    print("Tokenized words:", words)
    stop_words = set(stopwords.words('english'))
    stop_words.update(custom_stopwords)
#    print("stop_words = ",stop_words)
    doc = nlp(" ".join(words))  # Process text with spaCy
    # Filter words based on POS (keep only nouns, verbs, adjectives)
    filtered_words = [token.lemma_ for token in doc if
                      token.text.isalpha()  # Only keep alphabetic words
                      and token.lemma_ not in stop_words  # Remove stopwords
                      and len(token.lemma_) > 1       # Remove single character words
                      ]
#    print("filtered words = ", filtered_words)
    return filtered_words

def format_date(article):
    return datetime.strptime(article.date, "%Y-%m-%dT%H:%M:%SZ").strftime("%d/%m/%Y")

#To see how many articles mention the word and save it to a csv
def find_articles_containing_a_word_to_csv(articles, word_to_find, output_file):
    folder_path = "articles_with_the_word"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    full_file_path = os.path.join(folder_path, output_file)
    with open(full_file_path, mode="w", newline="")as file:
        writer = csv.writer(file)
        writer.writerow(["Section Name", "Date", "Web Title", "Web URL"])
        counter = 0
        for article in articles:
            if word_to_find in article.bodyText.lower():
                counter += 1
                try:
                    formatted_date = datetime.strptime(article.date, "%Y-%m-%dT%H:%M:%SZ").strftime("%d/%m/%Y")
                except ValueError:
                    # In case the date format is different or invalid
                    formatted_date = article.date  # Keep original date if parsing fails
                writer.writerow([article.sectionName, formatted_date, article.webTitle, article.webUrl])
                print(f"Exported {counter} articles containing '{word_to_find}' to {output_file}.")


def find_articles_containing_a_word(articles, word_to_find):
    # Prepare a list to hold filtered article data
    filtered_articles = []

    # Filter articles containing the keyword
    for article in articles:
        if word_to_find.lower() in article.bodyText.lower():
            try:
                # Format the date if necessary
                formatted_date = datetime.strptime(article.date, "%Y-%m-%dT%H:%M:%SZ").strftime("%d/%m/%Y")
            except ValueError:
                formatted_date = article.date  # Use the original date if parsing fails

            # Append relevant article details to the filtered list
            filtered_articles.append({
                "Section Name": article.sectionName,
                "Date": formatted_date,
                "Web Title": article.webTitle,
                "Web URL": article.webUrl
            })
    return filtered_articles


def get_bodytexts_in_section(articles, section):
    return [article.bodyText for article in articles if article.sectionName == section]
    if not articles:
        print(f"No articles found in the section: {section}")
        return []

def get_items_in_section(articles, section):
    return [article for article in articles if article.sectionName == section]
    if not articles:
        print(f"No articles found in the section: {section}")
        return []

def tokenized_words(articles):
    all_tokens = []
    for article in articles:
        tokens = preprocess_text(article)
        all_tokens.extend(tokens)
    return all_tokens

def get_top_keywords(word_counts, top_n):
    return word_counts.most_common(top_n)

def count_word_frequency(tokens):
    return Counter(tokens)

def word_frequency_in_section(articles, section, word):
    section_articles = get_bodytexts_in_section(articles, section)
    if not section_articles:
        print(f"No articles found in the section: {section}")
        return 0
    # Tokenize and preprocess the text for all articles in the section
    all_tokens = tokenized_words(section_articles)
    # Count the frequency of the word (case-insensitive)
    word_count = all_tokens.count(word.lower())  # Ensure case-insensitivity
    return word_count


def extract_keywords_from_section(articles, section, top_n=10):
    section_articles = get_bodytexts_in_section(articles, section)
    all_tokens = tokenized_words(section_articles)
    word_counts = count_word_frequency(all_tokens)
    # Get the most common words
    top_keywords = get_top_keywords(word_counts, top_n)
    return top_keywords

#to analyse the sentiment of articles

def analyse_sentiment_nltk(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    return sentiment['compound']

def interpret_sentiment(score):
    if score > 0.05:
        return "Positive"
    elif score < -0.05:
        return "Negative"
    else:
        return "Neutral"

def analyse_sentiment_by_section(articles, section):
    section_articles = get_items_in_section(articles, section)
    sentiment_results = []
    for article in section_articles:
        sentiment_score = analyse_sentiment_nltk(article.bodyText)
        classify_sentiment = interpret_sentiment(sentiment_score)
        sentiment_results.append((article.date, article.sectionName, article.webTitle, sentiment_score, classify_sentiment, article.webUrl))
    return sentiment_results

def export_sentiment_to_csv(sentiment_results, output_file):
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Section" , "Title", "Sentiment Score", "Sentiment Interpretation", "Web url"])
        for date, section, title, score, sentiment, weburl in sentiment_results:
            formatted_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").strftime("%d/%m/%Y")
            writer.writerow([formatted_date, section, title, score, sentiment, weburl])
    print(f"Sentiment analysis results exported to {output_file}")

def number_of_each_sentiment_label(sentiment_results, sentiment_label):
    counter = 0
    for date, section, title, score, sentiment, weburl in sentiment_results:
        if sentiment == sentiment_label:
            counter += 1
    print(f"Articles with {sentiment_label} sentiment: {counter}")



if __name__ == "__main__":
    test_text = "The new iPhone was announced by Apple, and it was said to be revolutionary."
    print(preprocess_text(test_text))