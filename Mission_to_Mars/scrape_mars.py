#!/usr/bin/env python
# coding: utf-8




# In[18]:


from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager


# In[19]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[20]:


# Open browser to NASA Mars News Site
browser.visit('https://mars.nasa.gov/news/')


# In[21]:


html = browser.html
soup = bs(html, 'html.parser')

# Search for news titles
# Search for paragraph text under news titles
news_title = soup.find("div", class_="content_title").get_text() 
news_p = soup.find("div", class_="article_teaser_body").get_text()

print(news_title)
print(news_p)

   


# In[22]:


# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[23]:


# Open browser to JPL Featured Image
browser.visit('https://spaceimages-mars.com')


# In[24]:


# Click through to find full image
browser.click_link_by_partial_text('FULL IMAGE')


# In[25]:


featured_image_path = soup.find_all('img')[2]["src"]
featured_image_url = 'https://spaceimages-mars.com'+ featured_image_path
print(featured_image_url)


# In[26]:


import pandas as pd


# In[27]:


url = 'https://galaxyfacts-mars.com/'
tables = pd.read_html(url)
tables
df = tables[1]
MarsFacts_df = df.rename(columns={0: "MarsFacts_name", 1: "MarsFacts_value"}, errors="raise")
MarsFacts_df.head()


# In[28]:


# Convert table to html
mars_facts_table = [df.to_html(classes='data table table-borderless', index=False, header=False, border=0)]
mars_facts_table


# In[29]:


# Store data in a dictionary
hemisphere_image_urls = [
    {"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/images/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg"},
    {"title": "Valles Marineris Hemisphere", "img_url": "https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg"},
]
hemisphere_image_urls


# In[31]:


FinalDictionary ={
    'news_title':news_title,
    'news_p': news_p,
    'featured_image_url' : featured_image_url,
    "tables":tables,
    'hemisphere' : hemisphere_image_urls
}
FinalDictionary


# In[ ]:





# In[ ]:





# In[ ]:




