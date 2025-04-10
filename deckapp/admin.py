from django.contrib import admin
from .models import DeckShuffle


@admin.register(DeckShuffle)
class DeckShuffleAdmin(admin.ModelAdmin):
    list_display = ('hash', 'count', 'created_at', 'last_seen')
    search_fields = ('hash',)
    ordering = ('-last_seen',)