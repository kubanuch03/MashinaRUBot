import requests
import csv
from  bs4 import BeautifulSoup
import urllib

def get_html(url):
    r = requests.get(url)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('ul', class_='pagination').find_all('a', class_='page-link')[-1].get('href')
    total_pages = pages.split('=')[1]
    return int(total_pages)

def write_csv(data):
    with open('mashina.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['title'],
                         data['price'],
                         data['url'],
                         data['img']))
def get_page_data(html):
    global url_1
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='listing search-page x-3').find_all('div', class_='listing-item main')

    for ad in ads[0:25]:
        try:
            title = ad.find('div', class_='sign b-l').find('span', class_='white font-big').text
        except:
            title = ''
        try:
            url = ad.find('a').get('href')
            url_1 = 'https//mashina.kg'+ url
        except:
            url = ''
        try:
            price = ad.find('div', class_='sign b-l').find('span', class_='custom-margins').text
        except:
            price = ''
        try:
            img = ad.find('div', class_='main-image').find('img').get('data-src')
        except:
            img = ''

        data = {
            'title': title,
            'price': price,
            'url': url_1,
            'img': img
        }
        write_csv(data)
def main():
    url = 'https://www.mashina.kg/new/search?page=1'
    base_url = 'https://www.mashina.kg/new/search?'
    page_part = 'page='

    total_pages = get_total_pages(get_html(url))

    for i in range(1, total_pages+1):
        url_gen = base_url+page_part+str(i)
        html = get_html(url_gen)
        get_page_data(html)
#+===========================+

def clear_code():
    lst = []
    with open('mashina.csv', 'r') as f:
        f = [i.split(',') for i in f]
        # len_lst = len(f)
        for i in range(0,40,2):    
            lst.append(f[i])
    return lst

def get_url(lst):
    urls = []
    for i in lst:
        urls.append(i[3])

    return urls
    
def get_img(urls):  
    len_urls = len(urls) 
    for i in range(len_urls):
        img = urllib.request.urlopen(urls[i]).read()
        out = open(f"img/img{i}.jpg", "wb")
        out.write(img)
        out.close
        
print(get_img(get_url(clear_code())))

if __name__ == '__main__':
    main()