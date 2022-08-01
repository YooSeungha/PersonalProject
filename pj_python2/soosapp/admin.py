from django.contrib import admin
from .models import Address


class findAddress(admin.ModelAdmin):
    search_fields = ['name','addr','rdate']

admin.site.register(Address,findAddress)

