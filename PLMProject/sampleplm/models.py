from django.db import models
from django.db.models.deletion import CASCADE

class plmProcessTracking(models.Model):
    
    plmStatusChoices = [('Queued','Queued'), ('Inprogress','Inprogress'), ('Failed', 'Failed'), ('Completed', 'Completed')]

    id = models.CharField(max_length=100, primary_key=True)
    serverName = models.CharField(max_length=100)
    plmStatus = models.CharField(max_length=45, choices=plmStatusChoices)
    changeNumber = models.CharField(max_length=100, null=True)
    plmStep = models.CharField(max_length=100, null=True)
    CreatedDate = models.DateTimeField(auto_now_add=True)


class PlmProcessResponse(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    plmStep = models.CharField(max_length=45)
    response = models.TextField(null=True)
    plm = models.ForeignKey(plmProcessTracking, on_delete=CASCADE)
    CreatedDate = models.DateTimeField(auto_now_add=True)