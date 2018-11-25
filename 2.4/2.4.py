from pprint import pprint
import json

with open('files/newsafr.json', encoding='utf-8') as datafile:
    json_data = json.load(datafile)
    for des in json_data['rss']['channel']['items']:
        print(des)


