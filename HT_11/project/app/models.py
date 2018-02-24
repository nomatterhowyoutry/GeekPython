from django.db import models
from django.contrib.postgres.fields import JSONField


# Create your models here.
class Stories(models.Model):
    data = JSONField(max_length=1000, null=True)
    id = models.IntegerField(primary_key=True, default=0)
    
    class Meta:
        abstract = True

class newstories(Stories):
    pass

class jobstories(Stories):
    pass

class showstories(Stories):
    pass

class askstories(Stories):
    pass