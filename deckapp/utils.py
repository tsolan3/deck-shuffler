import hashlib
import random
from django.utils import timezone
from .models import DeckShuffle

def generate_shuffled_deck():
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [f"{rank}{suit}" for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def get_deck_hash(deck):
    joined = ','.join(deck)
    return hashlib.sha256(joined.encode()).hexdigest()

def record_shuffle():
    deck = generate_shuffled_deck()
    deck_hash = get_deck_hash(deck)

    shuffle, created = DeckShuffle.objects.get_or_create(hash=deck_hash, defaults={
        'deck_order': ','.join(deck),
    })

    if not created:
        shuffle.count += 1
        shuffle.last_seen = timezone.now()
        shuffle.save()

    return {
        'deck': deck,
        'hash': deck_hash,
        'count': shuffle.count,
        'first_seen': shuffle.created_at,
        'last_seen': shuffle.last_seen,
    }
