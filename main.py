def get_list_top(string, symbol_count=5, quantity=3):
    result = ""
    list_big_word = {}
    for word in string.split(" "):
        if len(word) > symbol_count:
            list_big_word.update({word: list_big_word.get(word, 0) + 1})
    list_for_sort = list(list_big_word.items())
    list_for_sort.sort(key=lambda i: i[1], reverse=True)
    for item, _ in zip(list_for_sort, range(quantity)):
        result = result + " " + item[0]
    return result


import xml.etree.cElementTree as ET

tree = ET.parse("import.xml")
root = tree.getroot()
items = root.findall("channel/item")
words_array = ""
for item in items:
        words_array = words_array + " " + item.find("description").text
print(get_list_top(words_array, 6, 10))
