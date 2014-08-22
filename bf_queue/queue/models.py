from django.db import models
from model_utils.models import TimeStampedModel

class Queue(TimeStampedModel):
    type = models.CharField(max_length=10)
    message_id = models.CharField(max_length=200)
    target = models.CharField(max_length=200)
    message_count = models.IntegerField(default=1)
    message_count_total = models.IntegerField(default=1)
    message = models.TextField()
    error = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return "%s %s (%d of %d) %s %s" % (self.target,
                                self.message_id,
                                self.message_count,
                                self.message_count_total,
                                self.type,
                                self.message[0:50])
