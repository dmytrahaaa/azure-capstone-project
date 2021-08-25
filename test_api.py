from pathlib import Path
import csv
import requests
import time
import json

path = Path('./reddit_dataset.csv')
reddits = {}
URL = 'https://dmytraha3-uayd-func.azurewebsites.net/api/httptoeventhub?code=Odp/30pGWphsvaLi9VJ6iU71saEWcj1LlbT0w/zQGn2T9acev5ucBw=='

with open(path, encoding="utf8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        reddits[reader.line_num] = row

for i in reddits:
    subreddit = reddits[i]['subreddit']
    body = reddits[i]['body']
    data = {'subreddit': r'{0}'.format(subreddit),
            'body': r'{0}'.format(body),
            'time': str(time.time())
            }
    print(json.dumps(data))
    requests.post(url=URL, data=json.dumps(data))
    print(str(requests.post(url=URL, data=data).text))
    time.sleep(70)
