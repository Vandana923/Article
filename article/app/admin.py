from django.contrib import admin
from . models import article

# Register your models here.
@admin.register(article)
class articles(admin.ModelAdmin):
    list_display=["id","title","desc"]
