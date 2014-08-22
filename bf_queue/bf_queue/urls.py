from django.conf.urls import patterns, include, url
from django.contrib import admin
from uplink.api import UplinkResource
from downlink.api import DownlinkResource

admin.autodiscover()
uplink_resource = UplinkResource()
downlink_resource = DownlinkResource()

urlpatterns = patterns('',

    url(r'^api/v1/', include(uplink_resource.urls)),
    url(r'^api/v1/', include(downlink_resource.urls)),
    url(r'^admin/', include(admin.site.urls)),

)
