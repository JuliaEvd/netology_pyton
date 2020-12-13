import json
import xml.etree.ElementTree as ET


def print_sorted_data(data_dict, words_len, count):
    string_dict = dict()
    data_list = data_dict.lower().split()

    for word in data_list:
        if len(word) > words_len:
            if word in string_dict:
                string_dict[word] += 1
            else:
                string_dict.setdefault(word, 1)
    sorted_dict = sorted(string_dict.items(), key=lambda i: i[1], reverse=True)
    return sorted_dict[:count]


# открытие json
with open('newsafr.json', encoding='utf-8') as f:
    data = json.load(f)
    word_dict_json = {}
    descriptions = data["rss"]["channel"]["items"]
    json_descriptions = str()
    for description in descriptions:
        json_descriptions += str(description['description']).lower()

# открытие xml
parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()

news_list = root.findall('channel/item')
xml_descriptions = str()
for item in news_list:
    xml_descriptions += item.find('description').text.lower()

print(print_sorted_data(json_descriptions, 6, 10))
print(print_sorted_data(xml_descriptions, 6, 10))
