from django.shortcuts import render
from django.http import JsonResponse, Http404
from abyss.models import Quote
from datetime import datetime, timedelta

# Create your views here
def ajax_rating(request):
    if request.is_ajax():
        q_index = int(request.GET.get('q_index'))
        r_delta = int(request.GET.get('r_delta'))
        if request.COOKIES.get('r{}'.format(q_index)):
            response = JsonResponse({'error': 'Ви вже голосували раніше за цю цитату.'})
            response.status_code = 403
        else:
            quote = Quote.objects.get(pk=q_index)
            quote.rating = quote.rating + r_delta
            quote.save()
            response = JsonResponse({'message': 'Ви успішно проголосували за цитату.', 'q_index': q_index, 'rating': quote.rating})
            response.set_cookie('r{}'.format(q_index), 'true', expires=datetime.now() + timedelta(days=14), httponly=True)
        return response
    else:
        raise Http404('Невірна адреса')



def ajax_accordion(request):
    if request.is_ajax():
        q_index = int(request.GET.get('q_index'))
        if request.COOKIES.get('a{}'.format(q_index)):
            response = JsonResponse({'error': 'Ви вже повідомляли про цю цитату.'})
            response.status_code = 403
        else:
            quote = Quote.objects.get(pk=q_index)
            quote.accordion_rating += 1
            quote.save()
            response = JsonResponse({'message': 'Ви успішно повідомили про цю цитату.', 'q_index': q_index})
            response.set_cookie('a{}'.format(q_index), 'true', expires=datetime.now() + timedelta(days=14), httponly=True)
        return response
    else:
        raise Http404('Невірна адреса')

