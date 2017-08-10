import urllib
from urllib2 import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



TotAvg="points_total_career_season.htm, points_per_game_career_season.htm, points_total_single_season.htm, points_per_game_single_season.htm, points_total_career_playoffs.htm, http://www.landofbasketball.com/all_time_leaders/points_per_game_career_playoffs.htm, http://www.landofbasketball.com/all_time_leaders/points_total_single_playoffs.htm, http://www.landofbasketball.com/all_time_leaders/points_per_game_single_playoffs.htm"
url_template = "http://www.landofbasketball.com/all_time_leaders/{letter}.htm"
ALPL_df = pd.df()

for letter in TotAvg:
# url = "http://www.basketball-reference.com/draft/NBA_2014.html"
	url = url_template.format(letter=TotAvg)
	html = urlopen(url)
	soup = BeautifulSoup(html, "html5lib")

	# Getting Column Headers
	column_headers = [td.getText() for td in 
	                  soup.find_all('tr', limit=2)[1].find_all('td')]

	# getting the data
	data_rows = soup.find_all('tr')[2:]
	player_data = [[td.getText() for td in data_rows[i].find_all('td')]
	            for i in range(len(data_rows))]

	TotAvg_df = pd.DataFrame(player_data, columns=column_headers)
	TotAvg_df = df.replace(r'\n','', regex=True)
	TotAvg_df = df.replace(r',','', regex=True)
	df = df[:].fillna(0)
	df = df.convert_objects(convert_numeric=True)
	df = df.drop('', axis='columns')
	df = df.drop(df.index[25])

	df.to_csv('LOB_ATPL_SCT.csv', index=True, header=True)
# player_data_02 = []  # create an empty list to hold all the data

# for i in range(len(data_rows)):  # for each table row
#     player_row = []  # create an empty list for each pick/player

#     # for each table data element from each table row
#     for td in data_rows[i].find_all('td'):        
#         # get the text content and append to the player_row 
#         player_row.append(td.getText())        

#     # then append each pick/player to the player_data matrix
#     player_data_02.append(player_row)

# construct a pandas DataFrame

