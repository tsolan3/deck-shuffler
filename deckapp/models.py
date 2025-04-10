from django.db import models
from django.utils import timezone


class DeckShuffle(models.Model):
    hash = models.CharField(max_length=64, unique=True)
    deck_order = models.TextField()
    count = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Shuffle {self.hash[:8]}... seen {self.count}x"
