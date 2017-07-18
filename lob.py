import urllib
from urllib2 import urlopen
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def make_soup(url):
	thepage = urllib.urlopen(url)
	soupdata = BeautifulSoup(thepage, "html.parser")
	return soupdata

playerdatasaved=""
soup = make_soup("http://www.landofbasketball.com/all_time_leaders/points_total_career_season.htm")
for record in soup.find_all('tr'):
	playerdata=""
	for data in record.find_all(['th','td']):
		playerdata=playerdata+","+data.text
	if len(playerdata)!=0:
		playerdatasaved=playerdatasaved+"\n"+playerdata[1:]

#header="Player, From, To, Pos, Ht, Wt, Birth Date, College"
file=open('C:/users/hzhcui/desktop/scrapingnba/lob.csv',"wb")
#file.write(bytes(header))
file.write(bytes(playerdatasaved))

print(playerdatasaved)