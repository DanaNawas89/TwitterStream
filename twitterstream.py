from bs4 import BeautifulSoup
import requests
from datetime import datetime
import re


def user_tweets(DeepStateExpose, c):
    ctr = c  # '1000
    res = requests.get('https://twitter.com/' + DeepStateExpose)
    bs = BeautifulSoup(res.content, 'lxml')
    all_tweets = bs.find_all('div', {'class': 'tweet'})
    result = []

    if all_tweets:
        for tweet in all_tweets[:ctr]:
            content = tweet.find('div', {'class': 'content'})
            header = content.find('div', {'class': 'stream-item-header'})
            timestamp = content.find("span", class_="_timestamp").attrs["data-time"]
            time = str(datetime.fromtimestamp(int(timestamp)))
            m = content.find('p', {'class': 'TweetTextSize'}).text.replace("\n", " ").strip()
            message = time + ":" + re.sub(r'^https?:\/\/.*[\r\n]*', '', m, flags=re.MULTILINE)

            result.append(message)

    else:
        return "List is empty/account name not found."

    return result


user = input('user handle: DeepStateExpose')
twts = user_tweets(user, 5)
for t in twts:
    print('\n++++++++++++++++++++++++++++\n' + t)
