import requests
from bs4 import BeautifulSoup
import pprint

#pull response data from website page using requests.get
res = requests.get('https://news.ycombinator.com/news')
#parse response data from site in HTML and create object
soup = BeautifulSoup(res.text, 'html.parser')
#using css selectors, store list of links and votes
links = soup.select('.storylink')
subtext = soup.select('.subtext')

#sorts the stories from hn list of stories by the number of votes, with highest vote count first.
def sort_stories_by_votes(hnlist):
  return sorted(hnlist, key = lambda k:k['votes'], reverse = True)


#create list of link titles from links provided with votes over 100.
def create_custom_hn(links, subtext):
  hn = []
  for index, item in enumerate(links):
    title = item.getText()
    href = item.get('href', None)
    vote = subtext[index].select('.score')
    if len(vote):
      points = int(vote[0].getText().replace(' points', ''))
      if points > 100:
        hn.append({'title': title, 'link': href, 'votes': points})
  return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))