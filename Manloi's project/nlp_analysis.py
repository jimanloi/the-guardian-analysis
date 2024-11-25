
from textblob import TextBlob
import spacy
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('punkt')
from collections import Counter
import os
from _datetime import datetime
from nltk.util import ngrams

nlp = spacy.load("en_core_web_sm")

custom_stopwords = {'said', 'us', 'would', 'also', 'one', 'two', 'three', 'could', 'will', 'did', 'and', 'the', 'in',
                    'of', 'to', 'a', 'for', 'on', 'at', 'go','tell', 'find', 'say', 'take'}


# Text preprocessing: Remove unwanted characters
def preprocess_text(text):
    words = word_tokenize(text.lower())
#    print("Tokenized words:", words)
    stop_words = set(stopwords.words('english'))
    stop_words.update(custom_stopwords)
#    print("stop_words = ",stop_words)
    doc = nlp(" ".join(words))  # Process text with spaCy
    # Filter words based on POS (keep only nouns, verbs, adjectives)
    filtered_words = [token.lemma_ for token in doc if
                      token.text.isalpha()  # Only keep alphabetic words
                      and token.text not in stop_words  # Remove stopwords
                      and len(token.text) > 1
                      or token.pos_ == "PROPN"]  # Remove single character words
#    print("filtered words = ", filtered_words)
    return filtered_words



def extract_named_entities(text):
    """Extract named entities (persons, organizations, locations) using spaCy."""
    doc = nlp(text)
    entities = [ent.text for ent in doc.ents if ent.label_ in {"PERSON", "ORG", "GPE"}]
    return entities


def extract_keywords(text, n=10):
    """Extract top keywords or phrases from text."""
    # Preprocess the text
    tokens = preprocess_text(text)

    # Extract bigrams (phrases of 2 words)
    bigrams = list(ngrams(tokens, 2))
    phrases = [" ".join(gram) for gram in bigrams]

    # Combine tokens and bigrams
    all_terms = tokens + phrases

    # Count frequency
    term_counts = Counter(all_terms)

    # Return top N terms
    return term_counts.most_common(n)

def filter_articles_by_section(articles, section):
    return [article.bodyText for article in articles if article.sectionName == section]
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

# Sentiment analysis using TextBlob
def analyze_sentiment(text):
    blob = TextBlob(text)
    # Returns polarity score between -1 (negative) and 1 (positive)
    return blob.sentiment.polarity


def word_frequency_in_section(articles, section, word):
    section_articles = filter_articles_by_section(articles, section)
    if not section_articles:
        print(f"No articles found in the section: {section}")
        return 0
    # Tokenize and preprocess the text for all articles in the section
    all_tokens = tokenized_words(section_articles)
    # Count the frequency of the word (case-insensitive)
    word_count = all_tokens.count(word.lower())  # Ensure case-insensitivity
    return word_count


def extract_keywords_from_section(articles, section, top_n=10):
    section_articles = filter_articles_by_section(articles, section)
    all_tokens = tokenized_words(section_articles)
    # Count word frequency
    word_counts = count_word_frequency(all_tokens)
    # Get the most common words
    top_keywords = get_top_keywords(word_counts, top_n)
    return top_keywords


# Generate word cloud

def save_wordcloud(keywords, section_name, output_dir="wordclouds"):
    """
    Generate and save a word cloud image from keywords.

    :param keywords: List of tuples (word, frequency).
    :param section_name: Name of the section (used for filename).
    :param output_dir: Directory to save the word cloud images.
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Convert keywords to a dictionary for word cloud generation
    word_freq = dict(keywords)

    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(word_freq)

    # Create a unique filename using section name and timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{section_name.replace(' ', '_')}_{timestamp}.png"
    filepath = os.path.join(output_dir, filename)

    # Save the word cloud image
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(filepath, format="png")
    plt.close()

    print(f"Word cloud saved to: {filepath}")

