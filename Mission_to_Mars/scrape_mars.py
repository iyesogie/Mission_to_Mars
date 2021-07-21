#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import requests
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[6]:


# URL of page to be scraped
url = 'https://redplanetscience.com'


# In[7]:


# Retrieve page with the requests module
response = requests.get(url)

response


# In[8]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = bs(response.text, 'html.parser')
print(soup)

   


# In[9]:


news_title = soup.body.p.text
news_title


# In[10]:


news_p = soup.body.find_all('p')[1].text
news_p


# In[11]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[12]:


url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[13]:


button = browser.find_by_tag('button')[1]
button.click()


# In[14]:


soup = bs(browser.html, 'html.parser')
print(soup)


# In[15]:


featured_image = soup.find('img', class_='fancybox-image').get('src')

featured_image_url = url + '/' + featured_image
featured_image_url


# In[18]:


url = 'https://galaxyfacts-mars.com/'
tables = pd.read_html(url)
tables
df = tables[0]
df


# In[19]:


html_table = df.to_html()
html_table


# In[20]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[21]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

hemisphere_image_urls = []

url = 'https://marshemispheres.com/'
browser.visit(url)

html = browser.html
soup = bs(html, 'html.parser')

hemisphere_names = []

hemisphere_names = soup.find_all('h3')
hemisphere_names

for x in range(1,4):
   hemisphere_name = hemisphere_names[x].text
   
   browser.links.find_by_partial_text(hemisphere_name).click()
   
   html = browser.html
   
   soup = bs(html, 'html.parser')
   
   pic = soup.find_all('a',{'target':'_blank'})[3]['href']
   
   cerberus = {'title': hemisphere_name, 'img_url': pic}
   
   hemisphere_image_urls.append(cerberus)
   
   browser.links.find_by_partial_text('Back').click()


# In[22]:


hemisphere_image_urls


# In[ ]:




