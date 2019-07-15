from django.shortcuts import render
from text_strings.stringdata import strings

# Create your views here.
def about(request):
    return render(request, 'about.html', {'strings': strings['about']})