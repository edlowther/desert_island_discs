from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_track_listings(browser, url, existing_data):
    browser.set_window_size(1120, 550)
    browser.get(url)
    browser.execute_script("window.scrollTo(0, 800)")
    element = WebDriverWait(browser, 3).until(
       EC.presence_of_element_located((By.CLASS_NAME, "segments-list"))
    )
    guest_name = browser.find_elements_by_tag_name("h1")[0].text
    date = 'not listed'
    book_choice = 'not found'
    luxury_choice = 'not found'
    if len(browser.find_elements_by_class_name("broadcast-event__date")) > 0:
        date = browser.find_elements_by_class_name("broadcast-event__date")[0].text
    for segment__track in element.find_elements_by_class_name("segment__track"):
        artist = 'not listed'
        title = 'not listed'
        try:
            h3_list = segment__track.find_elements_by_tag_name("h3")
            if len(h3_list) > 0:
                artist = h3_list[0].text
            else:
                h4_list = segment__track.find_elements_by_tag_name("h4")
                if len(h4_list) > 0:
                    artist = h4_list[0].text
            ps = segment__track.find_elements_by_tag_name("p")
            if len(ps) > 0:
                title = ps[0].text
        except:
            print("data missing")
            print(segment__track.text.strip())
        finally:
            existing_data.append({
                'date': date,
                'url': url,
                'guest_name': guest_name,
                'category': 'song',
                'artist': artist,
                'title': title
            })
    for li in browser.find_elements_by_class_name("segments-list__item"):
        if 'BOOK CHOICE' in li.text:
            book_choice = li.text.replace('BOOK CHOICE', '').strip()
            existing_data.append({
                'date': date,
                'url': url,
                'guest_name': guest_name,
                'category': 'book',
                'artist': 'n/a',
                'title': book_choice
            })
        if 'LUXURY CHOICE' in li.text:
            luxury_choice = li.text.replace('LUXURY CHOICE', '').strip()
            existing_data.append({
                'date': date,
                'url': url,
                'guest_name': guest_name,
                'category': 'luxury',
                'artist': 'n/a',
                'title': luxury_choice
            })
        elif 'LUXURY ITEM' in li.text:
            luxury_choice = li.text.replace('LUXURY ITEM', '').strip()
            existing_data.append({
                'date': date,
                'url': url,
                'guest_name': guest_name,
                'category': 'luxury',
                'artist': 'n/a',
                'title': luxury_choice
            })
    return existing_data
