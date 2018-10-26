#!/usr/bin/python3

"""
    Script to download audio files from non-xml, non-rss, site
"""

import csv
from datetime import datetime
from bs4 import BeautifulSoup
import urllib
import re
#from mutagen.id3 import ID3,TDAT,TPOS1,TPOS2,TRCK,TIT2

site_url = 'https://centralteachings.com/4th-street/'
csv_file = 'results.csv'

#speaker = ''
#passage = ''
#title = ''
#CT_date = ''
#speaker_image = ''

audio_files = []
images = []
titles = []
passages = []
speakers = []

page = urllib.request.urlopen(site_url)
#print(page)
soup = BeautifulSoup(page,'html.parser')
#print(soup)
items = []
for x in soup.find_all('div',attrs={'class':'views-row'}):
    #print(x)
    for y in x.find_all('div',attrs={'class':'views-field-field-bio-picture'}):
        print(y)
        for z in str(y.div.img).split(" "):
            print(z)
            if z.find('.JPG') != -1:
                images.append(re.sub('"','',z.partition("=")[2]))
                print(images)
            if z.find('alt') != -1:
                speakers.append(re.sub('"','',z.partition("=")[2]))
                print(speakers) #needs to be gotten from elsewhere in case the 
                                #speaker doesn't have a photo to grab this from
    for title_tag in x.find_all('div',attrs={'class':'views-field-title'}):
        titles.append(str(title_tag.span.a.contents))
        print(titles)
    for passage_tag in x.find_all('div',attrs={'class':'views-field-field-passage'}):
        passages.append(str(passage_tag.div.contents))
        print(passages)
    for audio_tag in x.find_all('div',attrs={'class':'views-field-field-audio-link'}):
        for auditem in str(audio_tag.div.a).split(" "):
            print(auditem)
            if auditem.find('.m4a') != -1:
                print(auditem)
                audio_files.append(re.sub('"','',str(auditem)).partition("=")[2])
                print(audio_files)

for url in audio_files:
    print(url)
    urllib.request.urlretrieve(url,"file-" + re.sub("/","",url))

# TODO
# get most recent content
# get audio file, img, speaker, passage, title
# download audio file
# convert to mp3
# write metadata including date
