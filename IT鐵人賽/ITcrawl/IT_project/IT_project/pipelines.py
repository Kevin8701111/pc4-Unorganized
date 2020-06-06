# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
# from datetime import datetime
from datetime import date, timedelta, datetime
import re
import json
import logging
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from scrapy.exceptions import DropItem

class ItProjectPipeline(object):
    def process_item(self, item, spider):
        return item

class GoogleSheetPipeline(object):
    def auth_gss_client(self, path, scopes):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(path, scopes)
        return gspread.authorize(credentials)

    def open_spider(self, spider):
        auth_json_path = spider.settings.get('GOOGLE_SHEET_AUTH_PATH', './auth.json')
        gss_scopes = spider.settings.get('GSS_SCOPES', 'https://spreadsheets.google.com/feeds')
        gss_client = self.auth_gss_client(auth_json_path, gss_scopes)
        spred_sheet_url = spider.settings.get('SPREAD_SHEET_URL', 'https://docs.google.com/spreadsheets/d/18CcTmSknY50d6EsglE17P3LaBWE0aDxPMsBdP5karaM/edit#gid=0')
        sh = gss_client.open_by_url(spred_sheet_url)
        yesterday = date.today() - timedelta(1)
        self.title = yesterday.strftime("%B_%d_%Y")
        print(self.title)
        try:
            self.worksheet = sh.add_worksheet(title=self.title, rows="1000", cols="20")  # 建立新的 worksheet
        except:
            self.worksheet = sh.worksheet(self.title)
        
        # updata sheet's header
        head = ['Brand', 'StyleNumber', 'Name', 'Bullets', 'MinPrice', 'MaxPrice', 'Gender', 'Color',
            'Size', 'Sport', 'Clothing', 'AverageRating', 'ReviewNumber', 'ImageUrl', 'Url'] #sub 'Description',

        cell_list = self.worksheet.range('A1:O1')
        # Update values
        cell_index = 0
        for cell in cell_list:
            cell.value = head[cell_index]
            cell_index = cell_index + 1
        # Send update in batch mode
        self.worksheet.update_cells(cell_list)

    def process_item(self, item, spider):
        self.drop_item_by_product_name(item)
        self.product_price_fix(item)
        
        if item['AverageRating'] == None or item['AverageRating'] == []:
            item['AverageRating'] = 0.0
        if item['ReviewNumber'] == []:
            item['ReviewNumber'] = 0
        item['Bullets'] = [ b.replace('\n',' ') for b in item['Bullets']]
        item['Bullets'] = [ b.replace('\xa0',' ') for b in item['Bullets']]
        item['Bullets'] = [ b.replace(':',' ') for b in item['Bullets']]
        if spider.name == 'columbia':
            item['Bullets'] = [ b.replace('|',' ') for b in item['Bullets']]
        
        self.insert_product(item)
        return item

    def drop_item_by_product_name(self, item):
        filter_types = [
            'boots', 'tote', 'crevasse', 'watch', 'watches', 'glove', 'mittens', 'backpack', 'kabyte', 'kabig', 'kaban',
            'itinerant', 'gnomad', 'crevasse', 'toter', 'duffel', 'access', 'pack', 'bag', 'scrunchie', 'lanyard',
            'sunglasses', 'sackpack','shoe', 'belt', 'gaiter', 'kneepad', 'earphone', 'skateboard', 'slides', 'cleats',
            'spikes', 'wader','lacrosse', 'pads', 'mule', 'mitts', 'mitt', 'goggle', 'booties', 'bootie', 'shawl',
            'blanket', 'pouch', 'torque', 'mat', 'fastpack', 'puddle' , 'phone', 'strap', 'boot', 'soccer', 'benassi',
            'sack', 'sandals', 'sneaker', 'ball', 'cleat', 'slide', 'moc', 'sandal', 'cleat', 'slide', 'waistbag',
            'canteen', 'Hair Ties', 'Water Bottle', 'spray', 'lotion', 'co-wash', 'shampoo', 'sunscreen', 'pouch',
            'conditioner', 'balm', 
        ] 
        for t in filter_types:
            if t in item['Name'].lower(): 
                raise DropItem('found type Name : ', t)
            if t in item['Url'].lower():
                raise DropItem('found type Url : ', t)
            try:    
                if t in item['Clothing'].lower():
                    raise DropItem('found type :', t)
            except:
                pass

    def product_price_fix(self, item):

        
        item['MaxPrice'] = ('%.2f' % float(item['MaxPrice']))
        item['MinPrice'] = ('%.2f' % float(item['MinPrice']))
        # item['MaxPrice'] = str(float("{0:.2f}".format(float(item['MaxPrice'])))) 會自動去除重複的0
        # item['MinPrice'] = str(float("{0:.2f}".format(float(item['MinPrice'])))) 會自動去除重複的0

        if '$' in item['MinPrice']:
            item['MinPrice'] = item['MinPrice'].replace('$','')
            item['MaxPrice'] = item['MinPrice'].replace('$','')
        
        if (item['MinPrice'] == None or item['MinPrice'] == '' or item['MinPrice'] == '0') and (item['MaxPrice'] == None or item['MaxPrice'] == '' or item['MaxPrice'] == '0'):
            raise DropItem('found null MinPrice %s', item)

        if float(item['MinPrice']) > float(item['MaxPrice']) :
            mintemp = item['MaxPrice']
            item['MaxPrice'] = item['MinPrice']
            item['MinPrice'] = mintemp

        if float(item['MinPrice']) + float(item['MaxPrice']) == float(item['MaxPrice']) :
            item['MinPrice'] = item['MaxPrice']

        item['MinPrice'] = {
            'price':item['MinPrice'],
            'update_time':datetime.today().strftime('%Y-%m-%d')
            }

        item['MaxPrice'] = {
            'price':item['MaxPrice'],
            'update_time':datetime.today().strftime('%Y-%m-%d')
            }

    def insert_product(self, item):
        data = [
            str(item['Brand']), 
            str(item['StyleNumber']), 
            # str(item['Description']),
            str(item['Name']), 
            str(item['Bullets']),
            str(item['MinPrice']),
            str(item['MaxPrice']),
            str(item['Gender']),
            str(item['Color']),
            str(item['Size']),
            str(item['Sport']),
            str(item['Clothing']),
            str(item['AverageRating']),
            str(item['ReviewNumber']),
            str(item['ImageUrl']),
            str(item['Url']),
        ]
        self.worksheet.append_row(data)
        print('insert data to worksheet')

    def close_spider(self, spider):
        pass