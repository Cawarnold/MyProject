#!/usr/bin/env python
# -*- coding: utf-8 -*-

#### Scraping with lxml ####



## https://datawhatnow.com/introduction-web-scraping-python/

import requests
from lxml import html



url = 'https://www.datawhatnow.com'


def get_parsed_page(url):
 """Return the content of the website on the given url in
 a parsed lxml format that is easy to query."""
 
 response = requests.get(url)
 parsed_page = html.fromstring(response.content)
 return parsed_page

parsed_page = get_parsed_page(url)

# Print the website's title
print(parsed_page.xpath('//h1/a/text()'))  # ['Data, what now?']


# Print post names
print(parsed_page.xpath('//h2/a/text()'))
# Output
# ['SimHash for question deduplication',
#  'Feature importance and why it’s important']



# Getting paragraph titles in blog posts
post_urls = parsed_page.xpath('//h2//a/@href')
for post_url in post_urls:
    print('Post url:', post_url)
    
    parsed_post_page = get_parsed_page(post_url)
    paragraph_titles = parsed_post_page.xpath('//h3/text()')
    paragraph_titles = map(lambda x: ' \n  ' + x, paragraph_titles)
    print(''.join(paragraph_titles) + '\n')
# Output
# Post url: https://datawhatnow.com/simhash-question-deduplicatoin/
# 
#  SimHash 
#  Features 
#  Model performance 
#  Conclusion 
#  References 
#  Leave a Reply  
#  GitHub 
#  Newsletter 
#  Recent Posts 
#  Archives
#
# Post url: https://datawhatnow.com/feature-importance/
# 
#  Data exploration 
#  Feature engineering 
#  Baseline model performance 
#  Feature importance 
#  Model performance with feature importance analysis 
#  Conclusion 
#  Leave a Reply  
#  GitHub 
#  Newsletter 
#  Recent Posts 
#  Archives



















