# -*- coding: utf-8 -*-
from datetime import datetime
import scrapy
import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
import time
# from scrapy_project.items import ScrapyProjectItem

class AthletaSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['athleta.gap.com']
    start_urls = ['https://athleta.gap.com/browse/category.do?cid=1006482&mlink=44913,17610101,topNav_AllNew,visnav&clink=17610101']
    url = 'https://athleta.gap.com/browse/category.do?cid=1006482&mlink=44913,17610101,topNav_AllNew,visnav&clink=17610101'
    # driver = webdriver.Chrome(executable_path="/home/imac/Downloads/chromedriver")
    # driver.close()
    # def start_requests(self):
    #         url = "https://api.gap.com/ux/web/productdiscovery-web-experience/products/at?resId=913507241601081&abSeg=%7B%22pdpRedesign%22%3A%22Thumbnail2%22%2C%22pgGP%22%3A%22p%22%2C%22CSI%22%3A%22m2%22%2C%22gap03%22%3Anull%2C%22hc03%22%3A%22x%22%2C%22br03%22%3A%22x%22%2C%22at03%22%3A%22a%22%2C%22at01%22%3A%22x%22%2C%22at02%22%3A%22a%22%2C%22br02%22%3A%22a%22%2C%22gap02%22%3A%22a%22%2C%22gap01%22%3A%22x%22%2C%22hc01%22%3A%22a%22%2C%22hc02%22%3A%22a%22%2C%22br01%22%3A%22a%22%2C%22bopis-us-br%22%3A%22on%22%2C%22bopis-us-at%22%3A%22on%22%2C%22on06%22%3A%22a%22%2C%22br04%22%3A%22a%22%2C%22at04%22%3A%22a%22%2C%22br05%22%3A%22a%22%2C%22at05%22%3A%22a%22%2C%22m2%22%3A%22m2%22%2C%22c2%22%3A%22c2%22%2C%22v%22%3A%222%22%7D&cid=1006482&isFacetsEnabled=true&globalShippingCountryCode=us&globalShippingCurrencyCode=USD&locale=en_US"
    #         yield scrapy.Request(url, headers={'Content-Type':'application/json'}, callback = self.parse)
            # Content-Type: application/json;charset=UTF-8

    def parse(self, response):
        self.driver.get(self.url)

        time.sleep(5)

        self.driver.find_element_by_class_name("universal-modal__close-button").click()

        for i in range(1,51):
            n = str(i*200)
            b = "window.scrollBy(0,"+n+")"
            self.driver.execute_script(b)
            time.sleep(0.5)

        time.sleep(5)

        soup = BeautifulSoup(self.driver.page_source, 'lxml')

        product_links = soup.select('a.product-card__link')
        for link in product_links :
            url = link['href']
            
            

        # for product in soup.select('div.product-card__body'):
        #     print('-------------------------')
        #     print(product.select('a')[0]['href'])
 
        # body = soup.select('body')[0].text
        # try:
        #     for i in range(4):
        #         print('--------')
        #         try:
        #             for j in range(6):
        #                 api_size = api_json['productCategoryFacetedSearch']['searchFacetInfo']['searchFacetList'][1]['searchFacetOptionGroupList'][0]['searchFacetOptionGroupList']['searchFacetOptionGroupList'][i]['searchFacetOptionList'][j]['searchFacetOptionName']
        #                 print(api_size) 
        #         except:
        #             pass
        # except:
        #     pass

        # 印出size

        # try:
        #     for n in range(1,500):
        #         if n%2 != 0:
        #             K = body.replace('"businessCatalogItemId":','KKK').split('KKK')[n].split(',')[0].replace('"','')
        #             yield scrapy.Request('https://athleta.gap.com/browse/product.do?pid='+ K +'&cid=1124332&pcid=1006482&vid=1&grid=pds_0_171_1#pdp-page-content', callback = self.parse_detail)
        #         else:
        #             pass
        # except:
        #     pass

        # with open ('qwekk.json','a') as f:
        #     f.write(response.text)
       
        # api_name = api_json['productCategoryFacetedSearch']['productCategory']['childCategories'][0]['childProducts'][0]['name']
        # print(api_name)
       

    def parse_detail(self, response):
        # print('----hello----')
        # soup = BeautifulSoup(response.body, 'lxml')
        # name = soup.select('div.product-title')[0].text
        # print('---------')
        # print(name)
        pass

# averageRatnig / reviewNumber 的 url
# https://api.bazaarvoice.com/data/display/0.2alpha/product/summary?PassKey=7dtpedhgbgp2vn5p0ykid4opx&productid=486693012&contentType=reviews,questions&reviewDistribution=primaryRating,recommended&rev=0&contentlocale=en_US

# "parentSearchFacetOptionGroupId":"1",
# - XXS , XS , S , M , L , XL , 
# "parentSearchFacetOptionGroupId":"1",
# "searchFacetOptionGroupId":"1",
# "searchFacetOptionGroupName":"Regular"
# - 
# "parentSearchFacetOptionGroupId":"1",
# "searchFacetOptionGroupId":"2",
# "searchFacetOptionGroupName":"Tall"
# - 
# "parentSearchFacetOptionGroupId":"1",
# "searchFacetOptionGroupId":"3",
# "searchFacetOptionGroupName":"Petite"
# - XXS/XS , 

# "parentSearchFacetOptionGroupId":"2",

# "parentSearchFacetOptionGroupId":"3",
