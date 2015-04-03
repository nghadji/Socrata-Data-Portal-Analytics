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

#Specify the Socrata data portal:
startinglink = 'http://data.austintexas.gov/api/views'

#the name of the file to be created
filename = datetime.datetime.now().strftime('%d'+'%B'+'%I'+'%M'+'%p') + '_atxAnalysis' + '.csv'
#timeout = time.time() + 15 #*60? #timer used to test speed

RowNum = []
ID = []
Name = []
averageRating = []
category = []
createdAt = []
description = []
displayType = []
downloadCount = []
indexUpdatedAt = []
moderationStatus = []
numberOfComments = []
oid = []
publicationDate = []
publicationGroup = []
publicationStage = []
rowsUpdatedAt = []
rowsUpdatedBy = []
tableId = []
totalTimesRated = []
viewCount = []
viewLastModified = []
viewType = []


grants_flags = []
grants_type = []
grants_inh = []

owner_display = []
owner_id = []
owner_screenName = []
owner_rights = []

rights = []

tags = []
flags = []

tba_id = []
tba_dname = []
tba_sname = []

md_frequency = []
md_department = []
availableDisplayTypes = []
md_total = []

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

	try: averageRating.append(str(jsondata[i]["averageRating"]))
	except KeyError: 
		averageRating.append("n/a")
		pass

	try: category.append(str(jsondata[i]["category"]))
	except KeyError: 
		category.append("n/a")
		pass

	try: createdAt.append(str(jsondata[i]["createdAt"]))
	except KeyError: 
		createdAt.append("n/a")
		pass

	try: description.append(jsondata[i]["description"].encode('utf-8'))
	except KeyError: 
		description.append("n/a")
		pass

	try: displayType.append(str(jsondata[i]["displayType"]))
	except KeyError: 
		displayType.append("n/a")
		pass

	try: downloadCount.append(str(jsondata[i]["downloadCount"]))
	except KeyError: 
		downloadCount.append("n/a")
		pass

	try: indexUpdatedAt.append(str(jsondata[i]["indexUpdatedAt"]))
	except KeyError: 
		indexUpdatedAt.append("n/a")
		pass

	try: moderationStatus.append(str(jsondata[i]["moderationStatus"]))
	except KeyError: 
		moderationStatus.append("n/a")
		pass

	try: numberOfComments.append(str(jsondata[i]["numberOfComments"]))
	except KeyError: 
		numberOfComments.append("n/a")
		pass

	try: oid.append(str(jsondata[i]["oid"]))
	except KeyError: 
		oid.append("n/a")
		pass

	try: publicationDate.append(str(jsondata[i]["publicationDate"]))
	except KeyError: 
		publicationDate.append("n/a")
		pass

	try: publicationGroup.append(str(jsondata[i]["publicationGroup"]))
	except KeyError: 
		publicationGroup.append("n/a")
		pass

	try: publicationStage.append(str(jsondata[i]["publicationStage"]))
	except KeyError: 
		publicationStage.append("n/a")
		pass

	try: rowsUpdatedAt.append(str(jsondata[i]["rowsUpdatedAt"]))
	except KeyError: 
		rowsUpdatedAt.append("n/a")
		pass

	try: rowsUpdatedBy.append(str(jsondata[i]["rowsUpdatedBy"]))
	except KeyError: 
		rowsUpdatedBy.append("n/a")
		pass

	try: tableId.append(str(jsondata[i]["tableId"]))
	except KeyError: 
		tableId.append("n/a")
		pass

	try: totalTimesRated.append(str(jsondata[i]["totalTimesRated"]))
	except KeyError: 
		totalTimesRated.append("n/a")
		pass

	try: viewCount.append(str(jsondata[i]["viewCount"]))
	except KeyError: 
		viewCount.append("n/a")
		pass

	try: viewLastModified.append(str(jsondata[i]["viewLastModified"]))
	except KeyError: 
		viewLastModified.append("n/a")
		pass
		
	try: viewType.append(str(jsondata[i]["viewType"]))
	except KeyError: 
		viewType.append("n/a")
		pass

	try: grants_flags.append(str(jsondata[i]["grants"][0]["flags"][0]))
	except KeyError: 
		grants_flags.append("n/a")
		pass
	
	try: grants_type.append(str(jsondata[i]["grants"][0]["type"]))
	except KeyError: 
		grants_type.append("n/a")
		pass
	
	try: grants_inh.append(str(jsondata[i]["grants"][0]["inherited"]))
	except KeyError: 
		grants_inh.append("n/a")
		pass

	try: 
		s = ''
		for item in jsondata[i]["rights"]:
			s+= item + ', '
		rights.append(s[:-2])
	except KeyError: 
	 	rights.append("n/a")
	 	pass

	try: owner_display.append(str(jsondata[i]["owner"]["displayName"]))
	except KeyError: 
		owner_display.append("n/a")
		pass

	try: owner_id.append(str(jsondata[i]["owner"]["id"]))
	except KeyError: 
		owner_id.append("n/a")
		pass

	try: owner_screenName.append(str(jsondata[i]["owner"]["screenName"]))
	except KeyError: 
		owner_screenName.append("n/a")
		pass

	try: 
		s = ''
		for item in jsondata[i]["owner"]["rights"]:
			s+= item + ', '
		owner_rights.append(s[:-2])
	except KeyError: 
	 	owner_rights.append("n/a")
	 	pass

	try: 
		s = ''
		for item in jsondata[i]["tags"]:
			s+= item + ', '
		tags.append(s[:-2])
	except KeyError: 
	 	tags.append("n/a")
	 	pass

	try: 
		s = ''
		for item in jsondata[i]["flags"]:
			s+= item + ', '
		flags.append(s[:-2])
	except KeyError: 
	 	flags.append("n/a")
	 	pass

	try: tba_id.append(str(jsondata[i]["tableAuthor"]["id"]))
	except KeyError: 
		tba_id.append("n/a")
		pass
	
	try: tba_dname.append(str(jsondata[i]["tableAuthor"]["displayName"]))
	except KeyError: 
		tba_dname.append("n/a")
		pass
	
	try: tba_sname.append(str(jsondata[i]["tableAuthor"]["screenName"]))
	except KeyError: 
		tba_sname.append("n/a")
		pass

	try: md_total.append(str(jsondata[i]["metadata"]))
	except KeyError: 
		md_total.append("n/a")

	try: 
		s = ''
		for item in jsondata[i]["metadata"]["availableDisplayTypes"]:
			s+= item + ', '
		availableDisplayTypes.append(s[:-2])
	except KeyError: 
	 	availableDisplayTypes.append("n/a")
	 	pass

	try: md_frequency.append(str(jsondata[i]["metadata"]["custom_fields"]["Additional Information"]["Frequency"]))
	except KeyError: 
		md_frequency.append("n/a")

	try: md_department.append(str(jsondata[i]["metadata"]["custom_fields"]["Additional Information"]["Department"]))
	except KeyError: 
		md_department.append("n/a")

	i+=1
	RowNum.append(i)
	print "loop ",i," passed"

print "creating CSV..."
###this will take our data and put it into a new csv file, but we are missing headers
output=zip(RowNum,ID,Name,averageRating,category,createdAt,description,displayType,
downloadCount,indexUpdatedAt,moderationStatus,numberOfComments,oid,publicationDate,
publicationGroup,publicationStage,rowsUpdatedAt,rowsUpdatedBy,tableId,totalTimesRated,
viewCount,viewLastModified,viewType,rights,owner_display,owner_screenName,owner_id,
owner_rights,grants_flags,grants_type,grants_inh,tba_id,tba_dname,
tba_sname,tags,flags,md_frequency,md_department,
availableDisplayTypes,md_total)
f = open(filename, 'wb')
writer = csv.writer(f) ##opening a csv to write the file
df2 = writer.writerows(output)
f.close()

####this will write our headers
headers = ['Row_Num','ID','Name','Average_Rating','Category','Created_At','Description','Display_Type',
'Download_Count','Index_Updated_At','Moderation_Status','Number_Of_Comments','OID','Publication_Date',
'Publication_Group','Publication_Stage','Rows_Updated_At','Rows_Updated_By','Table_Id','Total_Times_Rated',
'View_Count','View_Last_Modified','View_Type','Rights','Owner Display Name','Owner Screen Name','Owner ID',
'Owner Rights','Grants Flags','Grants Type','Grants Inherited','Table_Author_Id','Table_Author_Display_Name',
'Table_Author_Screen_Name','Tags','Flags','Additional_Info_Frequency','Additional_Info_Department',
'Available Display Types','Metadata_Dump']


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

