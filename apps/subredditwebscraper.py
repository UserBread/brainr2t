import bs4
import requests
import json
from bs4 import BeautifulSoup
from bs4 import _typing

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

links = {
    "nosleep": [],
}



class MainPageWebscraper:
    def GetDailyLinks(self) -> dict[str, list[str]]:
        for subreddit in links.keys():
            res = requests.get(f'https://old.reddit.com/r/{subreddit}/', headers=headers)
            soup = BeautifulSoup(res.text, 'html.parser')

            for i in soup.find_all('a'):
                if i.has_attr('class'):
                    if i['class'] == ['title', 'may-blank']:
                        links[subreddit].append(f'https://old.reddit.com{i['href']}')

        return links

    def DisplayDailyLinks(self, links):
        for k, v in links.items():
            print(f'r/{k}', "------------------")
            for link in v:
                print(link)
