from collections import defaultdict

def count_articles_per_section_per_day(
    list: [], add_to_list: list[str]
) -> None:
    date_section_counts = defaultdict(lambda: defaultdict(int))
    for article in list:
        date_str = article.date.split('T')[0]
        if article.sectionName:
            date_section_counts[date_str][article.sectionName] += 1
    for date_str, sections in date_section_counts.items():
        for section, count in sections.items():
            add_to_list.append(f"{date_str} - {section}: {count}")
 #       print(f"section : {section}, article Count: {count}")
