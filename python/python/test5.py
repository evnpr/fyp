#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","","twitter_alerts" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM tweets WHERE text LIKE '%RT%'"

   # Execute the SQL command
cursor.execute(sql)
   # Fetch all the rows in a list of lists.
results = cursor.fetchall()

tweetid = []
tweetname = []
tweetnumberoffollower = []
weight = []
twit = []
twitUnique = []
listID = []
listNumFol = []

for row in results:
   #child data
   childid = row[1]
   text = row[2]
   screenname = row[3]
   numberOfFollower = row[4]
   
   #collect data   
   #tweetid.append(childid)
   #tweetname.append(screenname)
   #tweetnumberoffollower.append(numberOfFollower)
   #exec('id'+str(screenname)+'= '+str(childid))
   #exec('numfol'+str(screenname)+'= '+str(numberOfFollower))
   listID.append(('id'+str(screenname), childid))
   listNumFol.append(('numfol'+str(screenname), numberOfFollower))
   
getID = dict(listID)
getNumFol = dict(listNumFol)

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
      parentnumberoffollower = getNumFol['numfol'+parentname]
   except:
      continue
   
   t = parentid
   n = parentnumberoffollower

   twit.append((parentid, childid))

twitUnique = list(set(twit))

for itwit in twitUnique:
   #weight.append((itwit[0], itwit[1], twit.count(itwit)))
   print str(itwit[0])+" "+str(itwit[1])+"  "+str(twit.count(itwit))

# disconnect from server
db.close()