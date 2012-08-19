#!/usr/bin/python
import MySQLdb

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
   weight.append((childid, 0))
   
#lists of dict 1   
getID = dict(listID)
getNumFol = dict(listNumFol)
getNumFolID = dict(getNumFolID)



sql = "SELECT * FROM tweets WHERE text LIKE '%RT%'"

   # Execute the SQL command
cursor.execute(sql)
   # Fetch all the rows in a list of lists.
results = cursor.fetchall()


for row in results:
   #child data
   childid = row[1]
   text = row[2]
   screenname = row[3]
   numberOfFollower = row[4]
   
   
   #retrieve parent data
   try:
      after = text.split("RT @")[1]
      parentname = after.split(" ")[0].split(":")[0]
   except IndexError:
      continue
   
   try:
      parentid = getID['id'+parentname]
      getParentID.append((childid, parentid))
      parentnumberoffollower = getNumFol['numfol'+parentname]
      childnumberoffollower = getNumFol['numfol'+screenname]
   except:
      continue
   
   n = parentnumberoffollower
   cn = childnumberoffollower
   twit.append((parentid, childid, cn))


#lists of dict 2
getParentID = dict(getParentID)
weight = dict(weight)



def getRoot(id, i):
   try:
      weight[id] = weight[id] + getNumFolID[i]
      return getRoot(getParentID[id], i)
   except:
      return id



for itwit in twit:
   getRoot(itwit[1], itwit[1])
      
for itwit in twit:
   print itwit[0],
   print weight[itwit[0]]


# disconnect from server
db.close()