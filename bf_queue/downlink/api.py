__author__ = 'dev'
from tastypie.resources import ModelResource
from .models import Downlink


class DownlinkResource(ModelResource):
    class Meta:
        queryset = Downlink.objects.all()
        resource_name = 'downlink'