import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import requests
import os
from os.path import join, exists
from datetime import datetime, timedelta
from collections import defaultdict
import re
import numpy as np

def import_data_from_TheGuardian(api_key, api_endpoint, params, start_date, end_date):
    articles_dir = join('tempdata', 'articles')
    os.makedirs(articles_dir, exist_ok=True)
    # day iteration from here:
    # http://stackoverflow.com/questions/7274267/print-all-day-dates-between-two-dates
    dayrange = range((end_date - start_date).days + 1)
    for daycount in dayrange:
        dt = start_date + timedelta(days=daycount)
        datestr = dt.strftime('%Y-%m-%d')
        fname = join(articles_dir, datestr + '.json')
        if not exists(fname):
            # then let's download it
            print("Downloading", datestr)
            all_results = []
            params['from-date'] = datestr
            params['to-date'] = datestr
            current_page = 1
            total_pages = 1
            while current_page <= total_pages:
                print("...page", current_page)
                params['page'] = current_page
                resp = requests.get(api_endpoint, params)
                data = resp.json()
                all_results.extend(data['response']['results'])
                # if there is more than one page
                current_page += 1
                total_pages = data['response']['pages']

            with open(fname, 'w') as f:
                print("Writing to", fname)

                # re-serialize it for pretty indentation
                f.write(json.dumps(all_results, indent=2))

def get_readable_articles(list_to_work_on:[], folder_path, class_of_media):
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".json"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r') as file:
                data_of_the_day = json.load(file)  # TODO il faudra vérifier par la suite que ça reste "news of the day"
                if isinstance(data_of_the_day, list):
                    for article_data in data_of_the_day:
                        if article_data.get("type") == "article":
                            article = class_of_media(article_data)
                            list_to_work_on.append(article)
                else:
                    # If the data is a single article, process it directly
                    article = class_of_media(data_of_the_day)
                    list_to_work_on.append(article)
#    for article in list_of_all_articles:
#        print(article)


def count_articles_per_section_per_day(list, add_to_list:[]):
    date_section_counts = defaultdict(lambda: defaultdict(int))
    for article in list:
        date_str = article.date.split('T')[0]
        if article.sectionName:
            date_section_counts[date_str][article.sectionName] += 1
    for date_str, sections in date_section_counts.items():
        for section, count in sections.items():
            add_to_list.append(f"{date_str} - {section}: {count}")
 #       print(f"section : {section}, article Count: {count}")

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
    colors = plt.cm.get_cmap('tab20', num_sections)

    # Format the x-axis to display dates nicely
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=2))  # Adjust for more frequent ticks
    plt.xticks(rotation=45)

    # Y-axis from 0 to 250, with increments of 50
    plt.yticks(np.arange(0, 300, 50))

    # Add labels and legend
    plt.title("Number of Articles Per Section Per Day")
    plt.xlabel("Date")
    plt.ylabel("Number of Articles")
    plt.legend(loc='upper left', title='Sections', bbox_to_anchor=(1.05, 1), fontsize=8)

    # Show the plot
    plt.tight_layout()
    plt.savefig("stackplot1.png")

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

if __name__ == "__main__":
    pass



