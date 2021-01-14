import requests
from bs4 import BeautifulSoup

#pull response data from website page using requests.get
res = requests.get('https://news.ycombinator.com/news')
#parse response data from site in HTML and create object
soup = BeautifulSoup(res.text, 'html.parser')
#using css selectors, store list of links and votes
links = soup.select('.storylink')
votes = soup.select('.score')
votes.get()