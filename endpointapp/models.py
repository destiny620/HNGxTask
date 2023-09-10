from django.db import models
import datetime
# from datetime import datetime
import pytz
from datetime import date
import calendar
from django.utils import timezone



# Create your models here.

# def get_date():
#     today = datetime.datetime.now()
#     return today - datetime.timedelta(today.weekday())

def days():
    d = date.today()
    return calendar.day_name[d.weekday()]



def default_utc_time():
    return timezone.now()
    
 
class Endpoint(models.Model):
    slack_name = models.CharField(max_length=50)
    current_day = models.DateField(default=days, null=True)
    utc_time = models.DateTimeField(default=default_utc_time)
    track = models.CharField(max_length=50)
    github_file_url = models.CharField(max_length=200)
    gitup_repo_url = models.CharField(max_length=200)
    status_code = models.IntegerField(default=200)    
   
    
    def __str__(self):
        return self.slack_name + " " + self.track
      



