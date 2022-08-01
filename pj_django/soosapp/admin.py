from django.contrib import admin
from .models import Address, Board, Member


class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'addr', 'rdate']


class BoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'writer', 'subject', 'content', 'rdate']


class MemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'pwd', 'phone', 'rdate', 'udate']


admin.site.register(Address, AddressAdmin)
admin.site.register(Board, BoardAdmin)
admin.site.register(Member, MemberAdmin)
