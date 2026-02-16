from django.contrib import admin
from .models import Review


admin.site.register(Review)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'stars', 'comment')
    list_filter = ('stars',)
    search_fields = ('movie__title', 'comment')
