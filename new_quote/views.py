from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NewQuoteForm
from abyss.models import Quote

# Create your views here.
def new_quote_view(request):
    if request.method == 'POST':
        form = NewQuoteForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            body = form.cleaned_data['body']
            quote = Quote(email=email, body=body)
            quote.save()

            return HttpResponseRedirect('/abyss/')
    else:
        form = NewQuoteForm()
    return render(request, 'new_quote.html', {'form': form})