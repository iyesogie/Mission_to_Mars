#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install webdriver_manager')
get_ipython().system('pip install splinter')
get_ipython().system('pip install bs4')


# In[2]:


from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager


# In[3]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[4]:


# Open browser to NASA Mars News Site
browser.visit('https://mars.nasa.gov/news/')


# In[5]:


html = browser.html
soup = bs(html, 'html.parser')

# Search for news titles
# Search for paragraph text under news titles
news_title = soup.find("div", class_="content_title").get_text() 
news_p = soup.find("div", class_="article_teaser_body").get_text()

print(news_title)
print(news_p)

   


# In[6]:


# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[7]:


# Open browser to JPL Featured Image
browser.visit('https://spaceimages-mars.com')


# In[8]:


# Click through to find full image
browser.click_link_by_partial_text('FULL IMAGE')


# In[9]:


featured_image_path = soup.find_all('img')[2]["src"]
featured_image_url = 'https://spaceimages-mars.com'+ featured_image_path
print(featured_image_url)


# In[10]:


import pandas as pd


# In[11]:


url = 'https://galaxyfacts-mars.com/'
tables = pd.read_html(url)
tables
df = tables[1]
MarsFacts_df = df.rename(columns={0: "MarsFacts_name", 1: "MarsFacts_value"}, errors="raise")
MarsFacts_df.head()


# In[12]:


# Convert table to html
mars_facts_table = [df.to_html(classes='data table table-borderless', index=False, header=False, border=0)]
mars_facts_table


# In[15]:


# Store data in a dictionary
hemisphere_image_urls = [
    {"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/images/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg"},
    {"title": "Valles Marineris Hemisphere", "img_url": "https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg"},
]
hemisphere_image_urls


# In[21]:


get_ipython().system('pip install ipython')


# In[23]:


get_ipython().system('pip install nbconvert')


# In[25]:


jupyter nbconvert--to script [mission_to_mars].ipynb


# In[ ]:




