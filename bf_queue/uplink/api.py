__author__ = 'dev'
from tastypie.resources import ModelResource
from .models import Uplink


class UplinkResource(ModelResource):
    class Meta:
        queryset = Uplink.objects.all()
        resource_name = 'uplink'