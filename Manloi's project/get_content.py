import json
import requests
import os
from os.path import join, exists
from datetime import date, timedelta


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

if __name__ == "__main__":
    import_data_from_TheGuardian(api_key, api_endpoint, params, start_date, end_date)



