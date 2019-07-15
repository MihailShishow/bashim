from django.shortcuts import render
from abyss.models import Quote
from text_strings.stringdata import strings

# Create your views here.

def searchresults(request):
    q = request.GET.get('q')
    quotes = Quote.objects.filter(is_approved=True).filter(body__icontains=q).order_by("-approved_date")
    context = {'quotes': quotes, 'strings': strings['search_results']}
    return render(request, 'index.html', context=context)


def search(request):
    return render(request, 'search.html')