from django.contrib import admin
from .models import Uplink

class UplinkAdmin(admin.ModelAdmin):
    search_fields = ['type', 'message_id', 'target', 'message', 'error']
    # list_display = ['type', 'message_id', 'target', 'message', 'error']
    list_filter =  ['type', 'target']

admin.site.register(Uplink, UplinkAdmin)
