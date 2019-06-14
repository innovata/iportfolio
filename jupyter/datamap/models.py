
import os
import sys
sys.path.append(f"{os.getcwd()}/env/lib/python3.7/site-packages")
"""
"""
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "iportfolio.settings")
import django
django.setup()
#%env DJANGO_SETTINGS_MODULE="iportfolio.settings"
#%env PYTHONPATH="$PYTHONPATH:/Users/sambong/pjts/iportfolio"
#env

from iportfolio.wsgi import *
#os.environ["DJANGO_SETTINGS_MODULE"] = "iportfolio.settings"
#application = get_wsgi_application()
from django.db import models

# Create your models here.
models
class Keyword(models.Model):
    keyword = models.CharField(max_length=50)
    freq = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id} - {self.keyword} : {self.freq}"


class KeywordCombination(models.Model):
    combination = models.CharField(max_length=64)
    strength = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id} - {self.combination} : {self.strength}"
