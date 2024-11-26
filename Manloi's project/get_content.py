import json
import requests
import os
from os.path import join, exists
from datetime import timedelta


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
                try:
                    print(f"...Requesting page {current_page}")
                    params['page'] = current_page
                    resp = requests.get(api_endpoint, params)
                    resp.raise_for_status()  # Raise HTTPError for bad status codes
                    data = resp.json()

                    # Check for invalid response structure
                    if 'response' not in data or 'results' not in data['response']:
                        raise ValueError(f"Unexpected API response: {data}")
                    all_results.extend(data['response']['results'])
                # if there is more than one page
                    current_page += 1
                    total_pages = data['response']['pages']
                except requests.RequestException as e:
                    print(f"Error fetching data for {datestr}, page {current_page}: {e}")
                    break  # Exit pagination for this date
                except ValueError as e:
                    print(f"Error parsing API response: {e}")
                    break

            if all_results:
                try:
                    with open(fname, 'w') as f:
                        print(f"Writing to {fname}")
                        f.write(json.dumps(all_results, indent=2))
                except IOError as e:
                    print(f"Error writing file {fname}: {e}")

                # re-serialize it for pretty indentation
                f.write(json.dumps(all_results, indent=2))

def get_readable_articles(list_to_work_on:[], folder_path, class_of_media):
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".json"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r') as file:
                data_of_the_day = json.load(file)
                if isinstance(data_of_the_day, list):
                    for article_data in data_of_the_day:
                        if article_data.get("type") == "article":  #filter to have only articles
                            article = class_of_media(article_data)
                            list_to_work_on.append(article)
                else:
                    # If the data is a single article, process it directly
                    article = class_of_media(data_of_the_day)
                    list_to_work_on.append(article)
#    for article in list_of_all_articles:
#        print(article)






