from django.shortcuts import render
from abyss.models import Quote, get_similar_quotes
from django.http import Http404
from text_strings.stringdata import strings
import datetime
import statistics

# Create your views here.
def approved(request):
    quotes = Quote.objects.filter(is_approved=True).order_by("-approved_date")
    context = {'quotes': quotes, 'strings': strings['home']}
    return render(request, 'index.html', context=context)

def single_quote(request, quote_index):
    try:
        quote = Quote.objects.filter(id=quote_index)[0]

        context = {}
        context['quote'] = quote
        if request.user.is_authenticated:
            context['similar'] = get_similar_quotes(quote)

    except Quote.DoesNotExist:
        raise Http404('Цитата не існує.')

    return render(request, 'single.html', context=context)


def random_quotes(request):
    quotes = Quote.objects.filter(is_approved=True).order_by('?')[:50]
    context = {'quotes': quotes, 'strings': strings['random_quotes']}
    return render(request, 'index.html', context=context)


def by_rating(request):
    quotes = Quote.objects.filter(is_approved=True).order_by("-rating")
    context = {'quotes': quotes, 'strings': strings['by_rating']}
    return render(request, 'index.html', context=context)

def get_monday():
    today = datetime.datetime.now()
    today_weekday = today.isoweekday()
    monday = today - datetime.timedelta(days=today_weekday-1)
    return monday


def get_previous_week():
    today = datetime.datetime.now()
    today_weekday = today.isoweekday()
    sunday = today - datetime.timedelta(days=today_weekday)
    monday = sunday - datetime.timedelta(days=6)
    return (monday, sunday)

def get_min_best_rating(start_date, end_date=datetime.datetime.now()):
    quotes = Quote.objects.filter(is_approved=True).filter(approved_date__range=[start_date, end_date]).order_by('-rating')
    if quotes:
        ratings = []
        for quote in quotes:
            ratings.append(quote.rating)
        mode = statistics.mode(ratings)
    else:
        mode = None
    return mode



def best_quotes(request):
    prev_monday, prev_sunday = get_previous_week()
    monday = get_monday()
    today = datetime.datetime.now()

    mode_rating = get_min_best_rating(monday)
    quotes = Quote.objects.filter(is_approved=True).filter(approved_date__gt=monday).filter(rating__gt=mode_rating).order_by('-rating')
    if not quotes.exists():
        mode_rating = get_min_best_rating(prev_monday, prev_sunday)
        quotes = Quote.objects.filter(is_approved=True).filter(approved_date__range=[prev_monday, prev_sunday]).filter(rating__gt=mode_rating).order_by('-rating')
    context = {'quotes': quotes, 'strings': strings['best_quotes']}
    return render(request, 'index.html', context=context)
