from django.contrib import admin
from .models import React,Contact

# Register your models here.
admin.site.register(React)

# Create a custom admin class for the Contact model
class ContactAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


    def has_delete_permission(self, request, obj=None):
        return True

admin.site.register(Contact, ContactAdmin)
