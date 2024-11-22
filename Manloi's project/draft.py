import requests
import xml.etree.ElementTree as ET

class RSS:
    def __init__(self, source):
        response = requests.get(source, stream=True)
        response.raw.decode_content = True
        tree = ET.parse(response.raw)
        self.root = tree.getroot()

rssTheGuardian = RSS("https://www.theguardian.com/world")
print(rssTheGuardian.root[0][1].text)
for item in rssTheGuardian.root[0].findall('item'):
    print(f"{item[1].text}")

    delattr(data, 'body')
    delattr(data, "sectionId")
    delattr(data, "apiUrl")
    delattr(data, "fields.standfirst")
    delattr(data, "fields.trailText")

with open(file_path, 'r') as file:
    data = json.load(file)
    for key in keys_to_remove:
        if key in data:
            del data[key]
    for parent_key, child_key in nested_keys_to_remove.items():
        if parent_key in data:
            for child_key in child_keys:
                if child_key in data[parent_key]:
                    del data[parent_key][child_key]