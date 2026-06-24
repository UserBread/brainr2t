import requests
from bs4 import BeautifulSoup

class SubredditWebscraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        }
        self.links = {
            "nosleep": [],
        }

    def GetDailyLinks(self) -> dict[str, list[str]]:
        try:
            for subreddit in self.links.keys():
                res = requests.get(f'https://old.reddit.com/r/{subreddit}/', headers=self.headers)
                soup = BeautifulSoup(res.text, 'html.parser')

                for i in soup.find_all('a'):
                    if i.has_attr('class'):
                        if i['class'] == ['title', 'may-blank']:
                            self.links[subreddit].append(f'https://old.reddit.com{i['href']}')
            return self.links
        
        except Exception as e:
            print(f"Error occurred while fetching daily links: {e}")
            return self.links
    
    def GetPostText(self, link: str) -> str:
        try:
            res = requests.get(link, headers=self.headers)
            soup = BeautifulSoup(res.text, 'html.parser')
            body = soup.select_one('.entry.unvoted .usertext-body.may-blank-within.md-container')
            return body.get_text() if body else ""
        except Exception as e:
            print(f"Error occurred while fetching post text for link {link}: {e}")
            return ""

if __name__ == '__main__':
    srws = SubredditWebscraper()
    srws.GetDailyLinks()

    for k, v in srws.links.items():
        print(f'r/{k}', "------------------")
        for link in v:
            print(link)
            text = srws.GetPostText(link)
            print(text)