#!/usr/bin/python
import MySQLdb
import math

# Open database connection
db = MySQLdb.connect("localhost","root","","twitter_alerts" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM tweets"

   # Execute the SQL command
cursor.execute(sql)
   # Fetch all the rows in a list of lists.
results = cursor.fetchall()



#lists of lists
tweetid = []
tweetname = []
tweetnumberoffollower = []
weight = []
twit = []
twitUnique = []
listID = []
listNumFol = []
getParentID = []
getNumFolID = []

for row in results:
   #child data
   childid = row[1]
   text = row[2]
   screenname = row[3]
   numberOfFollower = row[4]
   
   #collect data   
   listID.append(('id'+str(screenname), childid))
   listNumFol.append(('numfol'+str(screenname), numberOfFollower))
   getNumFolID.append((childid, numberOfFollower))
   if(numberOfFollower!=0):
      initweight = math.log10(numberOfFollower)
   else:
      initweight = 1
   weight.append((childid, initweight))
   getParentID.append((childid, 01))
   twit.append(childid)
   
#lists of dict 1   
getID = dict(listID)
getNumFol = dict(listNumFol)
getNumFolID = dict(getNumFolID)
weight = dict(weight)
getParentID = dict(getParentID)
getParentIDdef = dict(getParentID)


twit = set(twit)



#
#for row in results:
#   #child data
#   childid = row[1]
#   text = row[2]
#   screenname = row[3]
#   numberOfFollower = row[4]
#   
#   
#   #retrieve parent data
#   try:
#      if text.split("RT @")[0]=='':
#         continue
#      after = text.split("RT @")[1]
#      parentname = after.split(" ")[0].split(":")[0]
#   except IndexError:
#      continue
#   
#   try:
#      parentid = getID['id'+parentname]
#      getParentID[childid] =  parentid
#   except:
#      continue
#   
#
#
#
#def getRoot(id, i):
#   try:
#      if id!=i:
#         weight[id] = weight[id] + math.log10(getNumFolID[i]*0.5)
#      if id!=getParentID[id] and id!=getParentID[getParentID[id]]:
#         return getRoot(getParentID[id], i)
#   except:
#      return id
#
#for itwit in twit:
#   getRoot(itwit, itwit)
#
#
#
#
##lists of lists
#listID = []
#listNumFol = []
#getParentID = getParentIDdef
#for row in results:
#   #child data
#   childid = row[1]
#   text = row[2]
#   screenname = row[3]
#   numberOfFollower = row[4]
#   
#   
#   #retrieve parent data
#   try:
#      if text.split("RT @")[0]!='':
#         continue
#      after = text.split("RT @")[1]
#      parentname = after.split(" ")[0].split(":")[0]
#   except IndexError:
#      continue
#   
#   try:
#      parentid = getID['id'+parentname]
#      getParentID[childid] = parentid
#   except:
#      continue
#   
#
#
#
#def getRoot2(id, i):
#   try:
#      if id!=i:
#         weight[id] = weight[id] + math.log10(getNumFolID[i]*0.3)
#      if id!=getParentID[id] and id!=getParentID[getParentID[id]]:
#         return getRoot2(getParentID[id], i)
#   except:
#      return id
#   
#for itwit in twit:
#   getRoot2(itwit, itwit)
#


#lists of lists
listID = []
listNumFol = []
getParentID = getParentIDdef
for row in results:
   #child data
   childid = row[1]
   text = row[2]
   screenname = row[3]
   numberOfFollower = row[4]
   
   
   #retrieve parent data
   try:
      if text.split("@")[0]!='':
         continue
      after = text.split("@")[1]
      parentname = after.split(" ")[0]
   except IndexError:
      continue
   
   try:
      parentid = getID['id'+parentname]
      getParentID[childid] = parentid 
   except:
      continue
   

def getRoot3(id, i):
   try:
      if id!=i:
         weight[id] = weight[id] + math.log10(getNumFolID[i]*0.2)
      if id!=getParentID[id] and id!=getParentID[getParentID[id]]:
         return getRoot3(getParentID[id], i)
   except:
      return id
   
for itwit in twit:
   getRoot3(itwit, itwit)






      
for itwit in twit:
   print itwit,
   print weight[itwit],
   print getNumFolID[itwit]


# disconnect from server
db.close()