#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","","twitter_alerts" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM tweets"
tweetid = []
tweetname = []
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      name = row[2]
      # Now print fetched result
      tweetid.append(id)
      tweetname.append(name)
      #print "id=%s" % \
      #       (fname)
except:
   print "Error: unable to fecth data"
   
print tweetid[tweetname.index('197jk')]

# disconnect from server
db.close()