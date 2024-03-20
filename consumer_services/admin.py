# gas_utility_project/consumer_services/admin.py
from django.contrib import admin
from .models import ServiceRequest, AccountInformation

# admin.site.register(ServiceRequest)
admin.site.register(AccountInformation)

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id','request_type', 'created_at', 'user','resolved_at', 'status')  # Add 'created_at' to the list_display
