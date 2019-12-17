import xml.etree.cElementTree as ET
from collections import Counter
import json

from prettytable import PrettyTable

def get_list_top(string, symbol_count=5, quantity=3):
    list_big_word = {}
    for word in string.split(" "):
        if len(word) > symbol_count:
            list_big_word.update({word.lower(): list_big_word.get(word, 0) + 1})
    list_for_sort = list(list_big_word.items())
    list_for_sort.sort(key=lambda i: i[1], reverse=True)
    return get_numbered_elements(list_for_sort, quantity)


def custom_print(table_data):
    for line in table_data:
        print(line[0], "cлово: ",line[1], "встретилось", line [2], " раз")

def get_numbered_elements(source_list, quantity=10):
    result = []
    i = 0
    for item, _ in zip(source_list, range(quantity)):
        i += 1
        result.append((i, item[0], item[1]))
    return result


def get_list_top2(string, symbol_count=5, quantity=3):
    def remove_short(x):
        if len(x) > symbol_count:
            return x

    value_counts = Counter(list(filter(remove_short, string.split(" "))))
    return get_numbered_elements(value_counts.most_common(), quantity)


def get_data_from_json(file):
    with open(file, 'r', encoding='utf-8') as fh:
        data = json.load(fh)
        words_array = ""
        for item in data["rss"]["channel"]["items"]:
            for word in item["description"].split(" "):
                words_array = words_array + " " + word.lower()
    return words_array


def get_data_from_xml(file):
    tree = ET.parse(file)
    root = tree.getroot()
    items = root.findall("channel/item")
    words_array = ""
    for item in items:
        temp = item.find("description").text
        words_array = words_array + temp.lower()
    return words_array

print("")
custom_print(get_list_top(get_data_from_xml("import.xml"), 6, 10))
print("")
custom_print(get_list_top(get_data_from_json("import.json"), 6, 10))

# добавил второй вариант. сомневаюсь на счет читаемости кода. нашел на хабре - решил попробовать.
print("")
custom_print(get_list_top2(get_data_from_xml("import.xml"), 6, 10))
print("")
custom_print(get_list_top2(get_data_from_json("import.json"), 6, 10))
