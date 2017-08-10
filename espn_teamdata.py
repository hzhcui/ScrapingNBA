import urllib
from urllib2 import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# url_template = "http://www.landofbasketball.com/all_time_leaders/{letter}.htm"

# url = "http://www.basketball-reference.com/draft/NBA_2014.html"
url = "http://espn.go.com/nba/teams"
html = urlopen(url)
soup = BeautifulSoup(html, "lxml")
tables = soup.find_all('ul', class_='medium-logos')

teams = []
prefix_1 = []
prefix_2 = []
teams_urls = []


for table in tables:
    lis = table.find_all('li')
    for li in lis:
        info = li.h5.a
        teams.append(info.text)
        url = info['href']
        teams_urls.append(url)
        prefix_1.append(url.split('/')[-2])
        prefix_2.append(url.split('/')[-1])


dic = {'url': teams_urls, 'prefix_2': prefix_2, 'prefix_1': prefix_1}
teams = pd.DataFrame(dic, index=teams)
teams.index.name = 'team'
print(teams)
teams.to_csv('espn_teams.csv', index=True, header=True)
# copper.save(teams, 'teams')