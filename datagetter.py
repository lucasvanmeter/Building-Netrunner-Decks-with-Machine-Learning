import requests
import json
import pandas as pd

# #make list of dates
# date1 = '2014-08-27'
# date2 = '2020-06-07'
# dates = pd.date_range(date1, date2).strftime('%Y-%m-%d')
# print(dates)

#open the file
f =  open('cards','w')

r =  requests.get('https://netrunnerdb.com/api/2.0/public/cards')
f.write(r.text)

# #we need to make a new json object containing each dates decklists json object
# f.write('{')

# #Write out into file
# for day in dates:
# 	r =  requests.get('https://netrunnerdb.com/api/2.0/public/decklists/by_date/'+day)
# 	f.write('"'+day+'": ['+r.text)
# 	f.write('],')

# #last one hardcoded so there is not comma at the end...
# lastday='2020-06-08'
# r =  requests.get('https://netrunnerdb.com/api/2.0/public/decklists/by_date/'+lastday)
# f.write('"'+lastday+'": ['+r.text)
# f.write(']')

# #end the json object and close the file
# f.write('}')

f.close()

#test loading the file
d = open('cards', 'r')
x = json.load(d)
d.close()

print(json.dumps(x, sort_keys=True, indent=4))
