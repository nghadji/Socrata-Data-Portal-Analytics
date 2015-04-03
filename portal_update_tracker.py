from __future__ import division
import json
import cookielib
from cookielib import CookieJar
import urllib2
from urllib2 import urlopen
import time
import datetime
import urllib
import csv
import string
from string import punctuation
import os
import fileinput
import sys
import pprint

##Need to tell server that you are a user and not a robot:
cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

print ""
print "Running code..."
print ""

#In case you want to search for a specific keyword/link/tag/etc here:
#keyWord = raw_input(">  ")
startinglink = 'http://data.austintexas.gov/api/views'

#the name of the file to be created
filename = datetime.datetime.now().strftime('%d'+'%B'+'%I'+'%M'+'%p') + '_dataset_updates' + '.csv'
#timeout = time.time() + 15 #*60? #timer used to test speed

RowNum = []
ID = []
Name = []
# averageRating = []
# category = []
createdAt = []
# description = []
# displayType = []
# downloadCount = []
indexUpdatedAt = []
# moderationStatus = []
# numberOfComments = []
# oid = []
publicationDate = []
# publicationGroup = []
# publicationStage = []
rowsUpdatedAt = []
rowsUpdatedBy = []
# tableId = []
# totalTimesRated = []
# viewCount = []
viewLastModified = []
# viewType = []


# grants_flags = []
# grants_type = []
# grants_inh = []

# owner_display = []
# owner_id = []
# owner_screenName = []
# owner_rights = []

# rights = []

# tags = []
# flags = []

# tba_id = []
# tba_dname = []
# tba_sname = []

# md_frequency = []
# md_department = []
# availableDisplayTypes = []
# md_total = []

sourceCode = opener.open(startinglink).read()
jsondata = json.loads(sourceCode)
LoopLength = len(jsondata)

i = 0

print "10 percent finished"

###here is where we grab the specific object(s) we want
while i < LoopLength:
	
	try: ID.append(str(jsondata[i]["id"]))
	except KeyError: 
		ID.append("n/a")
		pass

	try: Name.append(jsondata[i]["name"].encode('utf-8'))
	except KeyError: 
		Name.append("n/a")
		pass

	try: createdAt.append(str(jsondata[i]["createdAt"]))
	except KeyError: 
		createdAt.append("n/a")
		pass

	try: indexUpdatedAt.append(str(jsondata[i]["indexUpdatedAt"]))
	except KeyError: 
		indexUpdatedAt.append("n/a")
		pass

	try: publicationDate.append(str(jsondata[i]["publicationDate"]))
	except KeyError: 
		publicationDate.append("n/a")
		pass

	try: rowsUpdatedAt.append(str(jsondata[i]["rowsUpdatedAt"]))
	except KeyError: 
		rowsUpdatedAt.append("n/a")
		pass

	try: rowsUpdatedBy.append(str(jsondata[i]["rowsUpdatedBy"]))
	except KeyError: 
		rowsUpdatedBy.append("n/a")
		pass

	try: viewLastModified.append(str(jsondata[i]["viewLastModified"]))
	except KeyError: 
		viewLastModified.append("n/a")
		pass

	i+=1
	RowNum.append(i)
	print "loop ",i," passed"

print "creating CSV..."
###this will take our data and put it into a new csv file, but we are missing headers
output=zip(RowNum,ID,Name,createdAt,indexUpdatedAt,publicationDate,rowsUpdatedAt,rowsUpdatedBy,
viewLastModified)
f = open(filename, 'wb')
writer = csv.writer(f) ##opening a csv to write the file
df2 = writer.writerows(output)
f.close()

####this will write our headers
headers = ['Row_Num','ID','Name','Created_At','Index_Updated_At','Publication_Date','Rows_Updated_At','Rows_Updated_By','View_Last_Modified']


###this section will add the headers
tmp = open('TMP','w')
orig = open(filename, 'r')
tmp.write(','.join(headers)+'\n')
for line in orig.readlines():
    tmp.write(line)
orig.close()
tmp.close()
os.remove(filename)
os.rename('TMP',filename)

print "...Finished"
