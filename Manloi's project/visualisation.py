import re
import numpy as np
import itertools
import matplotlib.dates as mdates
from datetime import datetime
from collections import defaultdict
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def parse_data(list_to_work_on):
    date_section_counts = defaultdict(lambda: defaultdict(int))
    for entry in list_to_work_on:
        # Split the string to get date, section, and count
        date_str, section_info = entry.split(' - ', 1)
        match = re.match(r'^(.*?): (\d+)$', section_info)
        if match:
            section_name = match.group(1)
            count = int(match.group(2))
        # Add the count to the appropriate date and section
        date_section_counts[date_str][section_name] += count
    return date_section_counts


def prepare_data_for_stackplot(date_section_counts):
    # Sorting dates
    days = sorted(date_section_counts.keys())
    # Get unique sections from all data
    sections = sorted(
        set(section for section_dict in date_section_counts.values() for section in section_dict.keys()))
    # Prepare y_values for each section per day
    section_totals = {section: sum(date_section_counts[day].get(section, 0) for day in days) for section in sections}
    sorted_sections = sorted(section_totals.items(), key=lambda x: x[1], reverse=True)
    sorted_sections = [section for section, _ in sorted_sections]
    total_articles = sum(section_totals.values())
    # Step 2.4: Filter sections with less than 3% content
    sections_to_include = [section for section in sorted_sections if (section_totals[section] / total_articles) >= 0.03]

    # Step 2.5: Rearrange y_values to match the sorted section order, but only for sections to include
    y_values = []
    for day in days:
        day_counts = [date_section_counts[day].get(section, 0) for section in sections_to_include]
        y_values.append(day_counts)

    return days, sections_to_include, y_values, section_totals

    return days, sorted_sections, y_values


def plot_stackplot(days, sections, y_values, section_totals):
    # Convert the days from string to datetime
    days = [datetime.strptime(day, '%Y-%m-%d') for day in days]

    # Create the stackplot
    plt.figure(figsize=(12, 6))
    plt.stackplot(days, *zip(*y_values), labels=sections, alpha=0.8)

    # Create a color palette with one color per section
    num_sections = len(sections)
    # colors = plt.cm.get_cmap('tab20c', num_sections)  # Adjust based on the number of sections
    colors = itertools.cycle(plt.cm.tab20c.colors)
    color_list = [next(colors) for _ in sections]

    # Format the x-axis to display dates nicely
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=2))  # Adjust for more frequent ticks
    plt.xticks(rotation=45)

    # Y-axis from 0 to 250, with increments of 50
    plt.yticks(np.arange(0, 300, 50))

    # Add labels and legend
    plt.title("Number of Articles Per Section Per Day\n(section as defined by The Guardian website)")
    plt.xlabel("Date - month of October 2024")
    plt.ylabel("Number of Articles")
    plt.legend(loc='upper left', title='Sections', bbox_to_anchor=(1.05, 1), fontsize=8, reverse=True)

    # Show the plot
    plt.tight_layout()
    #  plt.show()
    plt.savefig("stackplot5.png")

    """
    sorted_section_counts = sorted(section_counts.items(), key=lambda x: x[1], reverse=True)
    sections = [section for section, count in sorted_section_counts]
    article_counts = [count for section, count in sorted_section_counts]


    section_counts = get_content.count_articles_by_attribute(list_of_all_articles)
    if section_counts:
        sorted_section_counts = sorted(section_counts.items(), key=lambda x: x[1], reverse=True)
        sections = [section for section, count in sorted_section_counts]
        article_counts = [count for section, count in sorted_section_counts]

     """


def plot_keywords(keywords, section, top_n=10, output_dir="wordclouds"):
    plt.figure(figsize=(10, 6))
    words, frequencies = zip(*keywords)
    plt.barh(words, frequencies, color='skyblue')
    plt.xlabel('Frequency')
    plt.ylabel('Keywords')
    plt.title(f"Top {top_n} Keywords in {section} section in The Guardian\nfrom 1 to 31 October 2024")
    plt.gca().invert_yaxis()  # Invert y-axis to have the highest frequency on top
    plt.tight_layout()
    # Create a unique filename using section name and timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{section.replace(' ', '_')}_{timestamp}_plot.png"
    filepath = os.path.join(output_dir, filename)
    plt.savefig(filepath, format="png")
    plt.close()
    print("plot saved.")

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
    print(f"Filepath: {filepath}")

    # Save the word cloud image
    try:
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.savefig(filepath, format="png")
        plt.close()
        print(f"Word cloud saved to: {filepath}")
    except Exception as e:
        print(f"Error saving word cloud: {e}")


if __name__ == "__main__":
    pass
