# -*- coding: utf-8 -*-
import scrapy
from IT_project.items import ProductItem
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime
import time
import json

class AthletaSpider(scrapy.Spider):
    name = 'athleta'
    allowed_domains = ['athleta.gap.com']
    start_urls = [
        # 'https://athleta.gap.com/browse/category.do?cid=1006482&mlink=44913,17610101,topNav_AllNew,visnav&clink=17610101',

        ]
    browser = webdriver.Firefox()

    num = 0
    today = str(datetime.date.today())

##### 這是拿取所有link的功能
    # def parse(self, response):
    #     self.browser.get(response.url)

    #     time.sleep(5)

    #     self.browser.find_element_by_class_name("universal-modal__close-button").click()

    #     for i in range(1,51):
    #         n = str(i*200)
    #         b = "window.scrollBy(0,"+n+")"
    #         self.browser.execute_script(b)
    #         time.sleep(0.5)

    #     time.sleep(5)

    #     soup = BeautifulSoup(self.browser.page_source, 'lxml')

    #     product_links = soup.select('a.product-card__link')
    #     for link in product_links :
    #         url = link['href']
    #         with open ('athleta.json','a', encoding="utf-8") as f:
    #             f.write('{"url":"'+url+'"},\n')
    #             print(url)

    def start_requests(self):
        href_json_file_path = '/home/kevin/IT鐵人賽/ITcrawl/IT_project/athleta.json'
        l = []
        with open (href_json_file_path) as f:
            links = json.load(f)
            for i in links:
                l.append(i['url'])
            urls = list(set(l))
            for url in urls:
                yield scrapy.Request(url, self.parse)

# ##### 這是拿取頁面資料的功能
    def parse(self, response):
        self.num = self.num + 1
        print(str(self.num) + ' : ' + response.url)
        self.browser.get(response.url)
        time.sleep(15)
        try:
            self.browser.find_element_by_class_name("universal-modal__close-button").click()
        except:
            pass
        time.sleep(5)
        soup = BeautifulSoup(self.browser.page_source, 'lxml')
        time.sleep(1)

        title = soup.select('h1.product-title__text')[0].text

        gender = 'women'

        try:
            prices = soup.select('h2')[0].text.split('$')
            maxprice = prices[2]
            minprice = prices[1].replace(' - ','')
        except:
            minprice = prices[1]
            maxprice = minprice
        
        # maxprice = "{'price': '" + maxprice + "', 'update_time': '" + self.today + "'}"
        # minprice = "{'price': '" + minprice + "', 'update_time': '" + self.today + "'}"

        color = [soup.select('div#swatch-label--Color span.label-value')[0].text]
        try:
            pf_bullets = soup.select('div.product-information-item')
            product_bullets = pf_bullets[0].text
            product_bullet = product_bullets.replace('Product Details','Product Details : ')
            fabric_bullets = pf_bullets[1].select('span')
        except:
            pass
        bullets = []
        try:
            for fabric_bullet in fabric_bullets:
                fabric = fabric_bullet.text+' '
                bullets.append(fabric)
            bullets.append(product_bullet)
        except:
            pass
        try:
            review_number = soup.select('button.bv_numReviews_text')[0].text
            average_rating = soup.select('button.bv_avgRating')[0].text
        except:
            pass
        if review_number == ' 0 Reviews':
            review_number = '0'
            average_rating = '0'
        else:
            review_number = review_number.split('(')[1].split(')')[0]

        brand = 'athleta'

        image_url = soup.select('div.product-photo a')[0]['href']
        image_url = 'https://athleta.gap.com'+image_url

        url = response.url
        

        size_all = soup.select('span.swatch__text')
        sizes = []
        for size in size_all:
            size = size.text
            sizes.append(size)

        style_number = product_bullets.rsplit('#')[1].split(')')[0]
        if  str(average_rating) == '':
            average_rating = '0'
        else:
            print('average_rating is error')

        item = ProductItem()
        item['Name'] = title
        item['Gender'] = gender
        item['MaxPrice'] = maxprice
        item['MinPrice'] = minprice
        item['Color'] = color
        item['Bullets'] = bullets
        item['ReviewNumber'] = review_number
        item['AverageRating'] = average_rating
        item['Description'] = ''
        item['Brand'] = brand
        item['ImageUrl'] = image_url
        item['Url'] = url
        item['Clothing'] = []
        item['Size'] = sizes
        item['Sport'] = []
        item['StyleNumber'] = style_number
        # print(item)
        yield item

        