import requests
import time
from lxml import html
import pickle

def get_urls():
    programme_urls = []
    for page_number in range(1,219):
        print(page_number)
        url = 'https://www.bbc.co.uk/programmes/b006qnmr/episodes/player?page={}'.format(page_number)
        index_html = html.fromstring(requests.get(url).text)
        for div in index_html.cssselect('.programme__body'):
            a = div.cssselect('a')[0]
            programme_urls.append(a.get('href'))
        time.sleep(0.2)
    print(programme_urls)
    print(len(programme_urls))
    with open('./data/programme_urls.pkl', 'wb') as f:
        pickle.dump(programme_urls, f)
