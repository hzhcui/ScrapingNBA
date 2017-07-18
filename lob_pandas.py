import urllib
from urllib2 import urlopen
from bs4 import BeautifulSoup
import html5lib
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

dfs = pd.read_html('http://www.landofbasketball.com/all_time_leaders/points_total_career_season.htm', header=0)
for df in dfs:
	print(df)

#header="Player, From, To, Pos, Ht, Wt, Birth Date, College"
file=open('C:/users/hzhcui/desktop/scrapingnba/lob_pandas.csv',"wb")
#file.write(bytes(header))
file.write(bytes(df))