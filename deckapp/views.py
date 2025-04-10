from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import F, Sum
from django.utils.dateformat import format as date_format

from .models import DeckShuffle
from .utils import record_shuffle


def api_shuffle(request):
    data = record_shuffle()
    return JsonResponse(data)


def main_page(request):
    return render(request, 'deckapp/main.html')


def hall_of_fame(request):
    top_shuffles = DeckShuffle.objects.filter(count__gt=1).order_by('-count', '-last_seen')[:10]
    total_shuffles = DeckShuffle.objects.aggregate(total=Sum('count'))['total'] or 0

    data = {
        'total_shuffles': total_shuffles,
        'entries': [
            {
                'deck': shuffle.deck_order.split(','),
                'hash': shuffle.hash,
                'count': shuffle.count,
                'first_seen': date_format(shuffle.created_at, 'Y-m-d H:i'),
                'last_seen': date_format(shuffle.last_seen, 'Y-m-d H:i'),
            }
            for shuffle in top_shuffles
        ]
    }
    return JsonResponse(data)