from django.db import models

class TweetsManager(models.Manager):
    def getNameRT(self):
        t = super(TweetsManager, self).get_query_set().filter(text__contains="RT")
        return t
    
    def getID(self, text):
        try:
            after = text.split("RT @")[1]
            name = after.split(" ")[0].split(":")[0]
        except IndexError:
            return 'bakso'
        try:
            t = super(TweetsManager, self).get_query_set().filter(screen_name=name)[0]
            return t.id
        except IndexError:
            return 'bakso'