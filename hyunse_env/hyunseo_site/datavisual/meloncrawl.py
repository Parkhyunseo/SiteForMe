# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import requests
from bs4 import BeautifulSoup
import csv

def melon_chart():
    chart_url = 'http://www.melon.com/chart/index.htm'
    html = requests.get(chart_url).text
    soup = BeautifulSoup(html, 'html.parser')
    melon_list = []
    
    with open('../static/csv/melon.csv','w') as csvFile:
        fieldnames = ['idx', 'tag', 'url']
        csv_writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
        csv_writer.writeheader()
        
        for idx, song_tag in enumerate(soup.select('#tb_list .lst50 a[href*=playSong]'), 1):
            menu_id, song_id = re.findall(r'\d+', song_tag['href'])
            song_url = 'http://www.melon.com/song/detail.htm?songId=' + song_id
            if idx <= 4:
                csv_writer.writerow({'idx': 240000-(idx*40000), 'tag': song_tag.text, 'url': song_url})
            else:
                csv_writer.writerow({'idx': 50000-(500*idx - idx*idx), 'tag': song_tag.text, 'url': song_url})
            melon_list.append((song_tag.text, song_url))
            print(idx, song_tag.text, '||', song_url)
        
    return melon_list
