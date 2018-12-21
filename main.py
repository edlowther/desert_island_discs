import pandas as pd
from selenium import webdriver
from src.get_track_listings import get_track_listings
from src.get_urls import get_urls
import pickle
import webbrowser

def pickle_me_now(programme_data, error_urls):
    with open('./data/programme_data.pkl', 'wb') as f:
        pickle.dump(programme_data, f)

    with open('./data/error_urls.pkl', 'wb') as f:
        pickle.dump(error_urls, f)


if __name__ == '__main__':
    """First, we need to get all the urls for the pages with song info on:
    """
    # get_urls()

    """Then we open up the pickle file with the urls in, and search each for
    the track listings:
    """
    # programme_urls = False
    # with open('./data/programme_urls.pkl', 'rb') as f:
    #     programme_urls = pickle.load(f)
    # print(len(programme_urls))
    # data = []
    # error_urls = []
    # count = 0
    # for url in programme_urls:
    #     print(count)
    #     print(url)
    #     count += 1
    #     browser = webdriver.Firefox()
    #     try:
    #         data = get_track_listings(browser, url, data)
    #     except KeyboardInterrupt:
    #         error_urls.append(url)
    #         pickle_me_now(data, error_urls)
    #         raise
    #     except:
    #         error_urls.append(url)
    #         pickle_me_now(data, error_urls)
    #     finally:
    #         pickle_me_now(data, error_urls)
    #         browser.quit()
    #
    # pickle_me_now(data, error_urls)
    """Check for errors

    """
    # error_urls = False
    # with open('./data/error_urls.pkl', 'rb') as f:
    #     error_urls = pickle.load(f)
    # print(len(error_urls))
    # for url in error_urls:
    #     webbrowser.open(url)

    """Finally, we convert the track info to a csv:
    """
    programme_data = False
    with open('./data/programme_data.pkl', 'rb') as f:
        programme_data = pickle.load(f)
    df = pd.DataFrame(programme_data)
    print(df.head())
    df[['date', 'guest_name', 'category', 'artist', 'title', 'url']].to_csv('desert_island_discs_v3.csv', index=False)
