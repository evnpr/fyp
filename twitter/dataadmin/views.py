from django.http import HttpResponse
from dataadmin.tweetsmodel import TweetsManager
from dataadmin.models import Tweets, Tweetsiphone

def android(request):
    output = Tweets.tweet.getNameRT()
    response = HttpResponse()
    response.write("""
                   <title>Twitter - FYP!</title>
                   """)
    twit = []
    numberOfRT = []
    for twet in output:
        t = Tweets.tweet.getID(twet.text)
        if (t!='bakso'):
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
#    sortedtwit = sorted(twit)
    
    for itwit in twit:
        twit2.append(itwit.split(" "))
        
    sortedtwit = sorted(twit2, key=lambda tup: int(tup[0]))
    twit = []
    
    for isortedtwit in sortedtwit:
        twit.append(sortedtwit.pop())
        
    for itwit in twit:
       response.write(itwit[0]+" "+itwit[1]+"<br>")

#    for itwit in sortedtwit:
#        response.write(itwit+"<br>")
        
    return response

def iphone(request):
    output = Tweetsiphone.tweet.getNameRT()
    response = HttpResponse()
    response.write("""
                   <title>Twitter - FYP!</title>
                   """)
    twit = []
    numberOfRT = []
    for twet in output:
        t = Tweetsiphone.tweet.getID(twet.text)
        if (t!='bakso'):
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
#    sortedtwit = sorted(twit)
    
    for itwit in twit:
        twit2.append(itwit.split(" "))
        
    sortedtwit = sorted(twit2, key=lambda tup: int(tup[0]))
    twit = []
    
    for isortedtwit in sortedtwit:
        twit.append(sortedtwit.pop())
        
    for itwit in twit:
       response.write(itwit[0]+" "+itwit[1]+"<br>")

#    for itwit in sortedtwit:
#        response.write(itwit+"<br>")
        
    return response