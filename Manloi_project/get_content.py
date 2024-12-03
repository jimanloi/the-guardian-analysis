import json
import requests
import os
from os.path import join, exists
from datetime import timedelta, datetime
from dateutil.parser import parse
from guardian import GuardianArticle


def import_data_from_TheGuardian(api_key, api_endpoint, start_date, end_date, folder_name):
    # articles_dir = join('articles')
    os.makedirs(folder_name, exist_ok=True)
    params = {
        'from-date': "",
        'to-date': "",
        'order-by': "newest",
        'show-fields': 'all',
        'page-size': 200,
        'api-key': api_key,
        'api_endpoint': api_endpoint,
    }
    # day iteration from here:
    # http://stackoverflow.com/questions/7274267/print-all-day-dates-between-two-dates
    dayrange = range((end_date - start_date).days + 1)
    for daycount in dayrange:
        dt = start_date + timedelta(days=daycount)
        datestr = dt.strftime('%Y-%m-%d')
        fname = join(folder_name, datestr + '.json')
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
                    resp = requests.get(params["api_endpoint"], params)
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
                        #    print(f"Writing to {fname}")
                        f.write(json.dumps(all_results, indent=2))
                except IOError as e:
                    print(f"Error writing file {fname}: {e}")

                # re-serialize it for pretty indentation
            #    f.write(json.dumps(all_results, indent=2))


def get_readable_articles(list_to_work_on: list, folder_path, class_of_media, start_date, end_date):
    start_date = start_date
    end_date = end_date
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".json"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r') as file:
                data_of_the_day = json.load(file)
                if isinstance(data_of_the_day, list):
                    for article_data in data_of_the_day:
                        if isinstance(article_data, dict) and article_data.get("type") == "article":  #filter to have only articles
                            pub_date_str = article_data.get("webPublicationDate", "")
                            if pub_date_str:
                                pub_date = parse(pub_date_str).date()
                                # Include articles within the specified date range
                                if start_date <= pub_date <= end_date:
                                    article = class_of_media(article_data)
                                    list_to_work_on.append(article)
                elif isinstance(data_of_the_day, dict):
                # If the data is a single article, process it directly
                    pub_date_str = data_of_the_day.get("webPublicationDate", "")
                    if pub_date_str:
                        pub_date = parse(pub_date_str).date()
                    # Include articles within the specified date range
                        if start_date <= pub_date <= end_date:
                            article = class_of_media(data_of_the_day)
                            list_to_work_on.append(article)
                else:
                    print(f"Invalid data format in file: {file_name}")
    return list_to_work_on
#    for article in list_of_all_articles:
#        print(article)
