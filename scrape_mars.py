from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd 
import requests


def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape()
browser = init_browser()
data = {}


#import pandas script here?

# URL of page to be scraped
url = 'https://mars.nasa.gov/news/'

# Retrieve page with the requests module
response = requests.get(url)
# Create BeautifulSoup object; parse with 'lxml'
soup = BeautifulSoup(response.text, 'lxml')

executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

# Visit url for latest news
news_url = "https://mars.nasa.gov/news/"
browser.visit(news_url)
html = browser.html

# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, "html.parser")

# Extract article title and paragraph text
article = soup.find("div", class_='list_text')
news_title = article.find("div", class_="content_title").text
news_p = article.find("div", class_ ="article_teaser_body").text
print(news_title)
print(news_p)

#scrape most recent news article
news_title = "NASA's Mars 2020 Rover Completes Its First Drive"

news_p = "In a 10-plus-hour marathon, the rover steered, turned and drove in 3-foot (1-meter) increments over small ramps."



# find images from link in homework
image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(image_url)

# pull the full image and browse to appropriate location on site
browser.click_link_by_partial_text('FULL IMAGE')
time.sleep(5)
browser.click_link_by_partial_text('more info')

html = browser.html
image_soup = BeautifulSoup(html, 'html.parser')

# Scrape the URL and save to variable
img_url = image_soup.find('figure', class_='lede').a['href']
featured_image_url = f'https://www.jpl.nasa.gov{img_url}'
print(featured_image_url)

# pull mars planet profile table to get facts about mars
facts_url = "https://space-facts.com/mars/"
browser.visit(facts_url)
html = browser.html

# scrape the table containing facts about Mars
table = pd.read_html(facts_url)
mars_facts = table[1]

mars_facts

hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hemi_url)
html = browser.html

#soup it
soup = BeautifulSoup(html, "html.parser")

#dictionary setup
hemisphere_image_urls = []

results = soup.find("div", class_ = "result-list" )
hemispheres = results.find_all("div", class_="item")

for hemisphere in hemispheres:
    title = hemisphere.find("h3").text
    end_link = hemisphere.find("a")["href"]
    image_link = "https://astrogeology.usgs.gov/" + end_link
    browser.visit(image_link)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    downloads = soup.find("div", class_= "downloads")
    image_url = downloads.find("a")["href"]
    
    
print(hemisphere_image_urls)

#store and close

mars= {
    "news_title": news_title,
    "featured_image_url": featured_image_url,
    "mars_facts": mars_facts,
    "hemisphere_image_urls": hemisphere_image_urls}

    browser.quit()

    
}
