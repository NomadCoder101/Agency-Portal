from django.contrib import admin

# Register your models here.
from .models import Page
from .forms import ContactForm


class PageAdmin(admin.ModelAdmin):
    list_display = ('title','update_date')
    ordering = ('title',)
    search_fields = ('title'),




admin.site.register(Page, PageAdmin)
