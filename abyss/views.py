from django.shortcuts import render
from . import models


# Create your views here.

def abyss(request):
    if request.is_ajax():
        pass
    else:
        quotes = models.Quote.objects.filter(is_approved=False).order_by('-post_date')
        context = {'quotes': quotes}
        return render(request, 'abyss.html', context=context)
