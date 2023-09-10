from django.db import models
import datetime
# from datetime import datetime
import pytz
from datetime import date
import calendar



# Create your models here.

# def get_date():
#     today = datetime.datetime.now()
#     return today - datetime.timedelta(today.weekday())

def days():
    d = date.today()
    return calendar.day_name[d.weekday()]


    
 
class Endpoint(models.Model):
    slack_name = models.CharField(max_length=50)
    current_day = models.DateField(default=days, null=True)
    utc_time = models.DateTimeField(datetime.datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
    track = models.CharField(max_length=50)
    github_file_url = models.CharField(max_length=200)
    gitup_repo_url = models.CharField(max_length=200)
    status_code = models.IntegerField(default=200)    
   
    
    def __str__(self):
        return self.slack_name + " " + self.track
      



