import json
import os
import pandas as pd

folder_path = "./tempdata/articles"

articles_list = []

keys_to_remove = ["id","sectionId","webUrl","apiUrl","isHosted"]
nested_keys_to_remove = {"fields":["headline", "standfirst", "trailText","main","body","newspaperPageNumber","wordcount","isInappropriateForSponsorship","isPremoderated","shouldHideAdverts","showInRelatedContent","thumbnail","lang","isLive","charCount","shouldHideReaderRevenue","showAffiliateLinks","bylineHtml","showTableOfContents"]}

for file_name in os.listdir(folder_path):
    if file_name.endswith(".json"):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            data = json.load(file)
            for key in keys_to_remove:
                if key in data:
                    del data{key}
            print(f"Removing key: {key}")
            for parent_key, child_keys in nested_keys_to_remove.items():
                if parent_key in data:
                    for child_key in child_keys:
                        if child_key in data[parent_key]:
                            del data[parent_key][child_key]
            print(f"Removing nested key: {child_keys} from {parent_key}")
            articles_list.append(data)
            print(articles_list[0])

#df = pd.DataFrame(articles_list)

#print(df.head())
