#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","","twitter_alerts" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM tweetsiphone WHERE text LIKE '%RT%'"

   # Execute the SQL command
cursor.execute(sql)
   # Fetch all the rows in a list of lists.
results = cursor.fetchall()

tweetid = []
tweetname = []
numberOfRT = []
twit = []

for row in results:
   #child data
   childid = row[0]
   text = row[1]
   screenname = row[2]
   
   #collect data   
   tweetid.append(childid)
   tweetname.append(screenname)
   
   #retrieve parent data
   try:
      after = text.split("RT @")[1]
      parentname = after.split(" ")[0].split(":")[0]
   except IndexError:
      continue

   if parentname in tweetname:
      parentid = tweetid[tweetname.index(parentname)]
   else:
      continue
   
   t = parentid
   inp = "0 "+str(t)
   if inp in twit:
     pos = twit.index(inp)
     numberOfRT.append(inp)
     twit[pos] = str(numberOfRT.count(inp))+" "+str(t)
   elif str(numberOfRT.count(inp))+" "+str(t) in twit:
     pos = twit.index(str(numberOfRT.count(inp))+" "+str(t))
     numberOfRT.append(inp)
     twit[pos] = str(numberOfRT.count(inp))+" "+str(t)  
   else:  
     twit.append(inp)



twit2=[]          

for itwit in twit:
    twit2.append(itwit.split(" "))

sortedtwit = sorted(twit2, key=lambda tup: int(tup[0]))
twit = []

for isortedtwit in sortedtwit:
    twit.append(sortedtwit.pop())
    
for itwit in twit:
   print itwit[0]+" "+itwit[1]
    


# disconnect from server
db.close()