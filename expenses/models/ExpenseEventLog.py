from uuid import uuid4
from django.db import models
import jsonfield

class ExpenseEventLog(models.Model):
    guid = models.UUIDField(default=uuid4())
    sequence = models.IntegerField()
    data = jsonfield.JSONField()
    time = models.DateTimeField(auto_now_add=True)

    unique_together = (("guid", "sequence"),)