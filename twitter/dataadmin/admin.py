from django.contrib import admin
from dataadmin.models import Tweets, Tweetsiphone

class TweetsAdmin(admin.ModelAdmin):
  list_display = ('screen_name','text', 'followers_count')
  search_fields = ['screen_name', 'text', 'id']
  ordering = ['-followers_count']
  
admin.site.register(Tweets, TweetsAdmin)
admin.site.register(Tweetsiphone, TweetsAdmin)

