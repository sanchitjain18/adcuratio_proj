import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import urllib.parse

class Scrapper:
    def __init__(self, url="", conn=""):
        self.url = url
        self.conn = conn
        self.L1 = []
        self.L2 = []

    def dbCon(self):
        client = MongoClient(self.conn)
        db = client['ycombinator_sc_data']
        r1 = db.url_heading
        r1.insert_many(self.L1)
        r2 = db.url_metadata
        r2.insert_many(self.L2)
        print('Insertion in DB completed !!')

    def scrap(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        res = soup.find_all('tr', class_='athing')
        for i in res:
            p = i
            q = i.find_next_sibling('tr')

            dict = {}
            dict['link'] = p.find("a", class_='storylink').get('href')
            dict['heading'] = p.find("a", class_='storylink').text
            self.L1.append(dict)

            dict = {}
            dict['link'] = p.find("a", class_='storylink').get('href') if p.find(
                "a", class_='storylink') is not None else 'None'
            dict['Title'] = p.find("a", class_='storylink').text if p.find(
                "a", class_='storylink') is not None else 'None'
            dict['Author'] = q.find("a", class_='hnuser').text if q.find(
                "a", class_='hnuser') is not None else 'None'
            dict['Votes'] = q.find("span", class_='score').text if q.find(
                "span", class_='score') is not None else 'None'
            self.L2.append(dict)

        print('Scrapping completed !!')


url = 'https://news.ycombinator.com/'
conn = "mongodb+srv://sanchit3:"+urllib.parse.quote_plus("Q@sef123")+"@cluster0.goinv.mongodb.net/sanchit3"

s = Scrapper(url, conn)

s.scrap()

s.dbCon()