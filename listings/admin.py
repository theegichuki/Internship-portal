from django.contrib import admin

# Register your models here.

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'rate', 'list_date', 'recruiter')
    list_display_links = ('id', 'title')
    list_filter = ('recruiter',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'county', 'city', 'rate', 'company')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
