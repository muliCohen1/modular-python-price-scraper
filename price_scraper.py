import requests
from bs4 import BeautifulSoup
import re
import time
import email_sender
import input_output

class Product:
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
        }
    def __init__(self, url, title_selector, price_selector):
            self.url = url
            self.title_selector = title_selector
            self.price_selector = price_selector
            try:
                self.scrape()
            except AttributeError:
                email_sender.send("Something went wrong - Probably the scraped element no longer exists", self.url)

    def scrape(self):
        page = requests.get(self.url, headers = self.headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find(self.title_selector[0], self.title_selector[1]).get_text()
        price = re.sub("[^0-9]", "", soup.find(self.price_selector[0], self.price_selector[1]).get_text())[:4]
        title = re.sub(r'[^\x00-\x7F]+',' ', "".join(filter(lambda c: not (ord(c) >= 1424 and ord(c) <= 1514), title))).strip() #remove all non ascii after removing all heb characters
        read_value = input_output.read_file(title)
        if read_value != price:
            input_output.write_file(title, price)
            # email_sender.send([title, price, read_value], self.url)
        print(title + " is only " + price)

while True:
    bassbreaker = Product("https://www.kley-zemer.co.il/%D7%9E%D7%92%D7%91%D7%A8_%D7%9E%D7%A0%D7%95%D7%A8%D7%95%D7%AA_15_%D7%95%D7%95%D7%90%D7%98_fender_bassbreaker_15_combo", ["div", {"class": "title"}],  ["div", {"class": "saleprice"}])

    bj_iv = Product("https://www.kley-zemer.co.il/fender-blues-junior-iv", ["div", {"class": "title"}], ["div", {"class": "saleprice"}])

    bj_tweed = Product("https://www.kley-zemer.co.il/%D7%9E%D7%92%D7%91%D7%A8%D7%99%D7%9D_%D7%9C%D7%92%D7%99%D7%98%D7%A8%D7%95%D7%AA_fender_blues_junior_lacquered_tweed", ["div", {"class": "title"}],  ["div", {"class": "saleprice"}])

    yamaha_990 = Product("https://www.kley-zemer.co.il/%D7%A4%D7%A1%D7%A0%D7%AA%D7%A8_%D7%93%D7%99%D7%92%D7%99%D7%98%D7%9C%D7%99_yamaha_np12", ["div", {"class": "title"}], ["div", {"class": "saleprice"}])

    yamaha_fg800 = Product("https://www.kley-zemer.co.il/%D7%92%D7%99%D7%98%D7%A8%D7%95%D7%AA_%D7%90%D7%A7%D7%95%D7%A1%D7%98%D7%99%D7%95%D7%AA_yamaha_fg800_sunburst", ["div", {"class": "title"}], ["div", {"class": "saleprice"}])

    yamaha_fs800 = Product("https://www.kley-zemer.co.il/%D7%92%D7%99%D7%98%D7%A8%D7%95%D7%AA_%D7%90%D7%A7%D7%95%D7%A1%D7%98%D7%99%D7%95%D7%AA_yamaha_fs-800", ["div", {"class": "title"}], ["div", {"class": "saleprice"}])

    yamaha_fg830 = Product("https://www.kley-zemer.co.il/%D7%92%D7%99%D7%98%D7%A8%D7%94_%D7%90%D7%A7%D7%95%D7%A1%D7%98%D7%99%D7%AA_yamaha_fg830", ["div", {"class": "title"}], ["div", {"class": "saleprice"}])

    yamaha_fg820 = Product("https://www.kley-zemer.co.il/%D7%92%D7%99%D7%98%D7%A8%D7%95%D7%AA_%D7%90%D7%A7%D7%95%D7%A1%D7%98%D7%99%D7%95%D7%AA_yamaha_fg820_sunburst", ["div", {"class": "title"}], ["div", {"class": "saleprice"}])

    fender_pm2 = Product("https://www.kley-zemer.co.il/%D7%92%D7%99%D7%98%D7%A8%D7%94_%D7%90%D7%A7%D7%95%D7%A1%D7%98%D7%99%D7%AA_%D7%9E%D7%95%D7%92%D7%91%D7%A8%D7%AA_fender_pm2_standard_parlor", ["div", {"class": "title"}], ["div", {"class": "saleprice"}])
    
    martin_000x1ae = Product("https://www.avigil.co.il/product/%d7%92%d7%99%d7%98%d7%a8%d7%94-%d7%90%d7%a7%d7%95%d7%a1%d7%98%d7%99%d7%aa-%d7%9e%d7%95%d7%92%d7%91%d7%a8%d7%aa-martin-000x1ae", ["h1", {"class": "product-title"}],  ["div", {"class": "price-wrapper"}])

    martin_00x1ae = Product("https://www.avigil.co.il/product/%d7%92%d7%99%d7%98%d7%a8%d7%94-%d7%90%d7%a7%d7%95%d7%a1%d7%98%d7%99%d7%aa-%d7%9e%d7%95%d7%92%d7%91%d7%a8%d7%aa-martin-00lx1ae", ["h1", {"class": "product-title"}],  ["div", {"class": "price-wrapper"}])

    martin_jr_sap = Product("https://www.avigil.co.il/product/%d7%92%d7%99%d7%98%d7%a8%d7%94-%d7%90%d7%a7%d7%95%d7%a1%d7%98%d7%99%d7%aa-%d7%9e%d7%95%d7%92%d7%91%d7%a8%d7%aa-%d7%9e%d7%a8%d7%98%d7%99%d7%9f-martin-dreadnought-junior-2e-sapele", ["h1", {"class": "product-title"}],  ["div", {"class": "price-wrapper"}])

    martin_jr_spr = Product("https://www.avigil.co.il/product/%d7%92%d7%99%d7%98%d7%a8%d7%94-%d7%90%d7%a7%d7%95%d7%a1%d7%98%d7%99%d7%aa-%d7%9e%d7%95%d7%92%d7%91%d7%a8%d7%aa-martin-dreadnought-junior", ["h1", {"class": "product-title"}],  ["div", {"class": "price-wrapper"}])

    guild = Product("https://www.halilit.com/items/2647867-Guild-DS-240-Memoir-Slope-shoulde-", ["span", {"itemprop": "name"}],  ["span", {"class": "price_value"}])

    seagull1 = Product("https://www.wildguitars.co.il/product/seagull-s6-original-qi/", ["h1", {"class": "product_title"}],  ["p", {"class": "price"}])

    seagull2 = Product("https://www.wildguitars.co.il/product/seagull-s6-classic-m450t/", ["h1", {"class": "product_title"}],  ["p", {"class": "price"}])

    up_test = Product("https://kidkeep.co.il/testing/xyz.html", ["div", {"class": "sbj"}],  ["div", {"class": "num"}])

    time.sleep(3600)

