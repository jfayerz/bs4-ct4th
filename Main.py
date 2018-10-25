#!/usr/bin/python3

"""
    Script to download audio files from non-xml, non-rss, site
"""

import csv
from datetime import datetime
from bs4 import BeautifulSoup
import urllib
import re
from mutagen.id3 import ID3,TDAT,TPOS1,TPOS2,TRCK,TIT2

site_url = 'https://centralteachings.com/4th-street/'
csv_file = 'results.csv'

speaker = ''
passage = ''
title = ''
CT_date = ''
speaker_image = ''

audio_files = []
images = []
titles = []
passages = []
speakers = []

page = urllib.request.urlopen(site_url)
soup = BeautifulSoup(page,'html.parser')
items = []
for x in soup.find_all('div',attrs={'class':'views-row'}):
    items.append(x)

# TODO
# get most recent content
# get audio file, img, speaker, passage, title
# download audio file
# convert to mp3
# write metadata including date
