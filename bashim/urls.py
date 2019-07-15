"""bashim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from new_quote.views import new_quote_view
from approved_quotes.views import approved, single_quote, random_quotes, by_rating, best_quotes
from abyss.views import abyss
from search.views import search, searchresults
from ajax.views import ajax_rating, ajax_accordion
from about.views import about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('abyss/', abyss, name='abyss'),
    path('new/', new_quote_view, name='new'),
    path('', approved, name='index'),
    path('search/', search, name='search'),
    path('searchresults/', searchresults, name='searchresults'),
    path('quote/<int:quote_index>/', single_quote, name='singlequote'),
    path('ajax/rating/', ajax_rating, name='ajax_rating'),
    path('ajax/accordion/', ajax_accordion, name='ajax_accordion'),
    path('random/', random_quotes, name='random'),
    path('byrating/', by_rating, name='by_rating'),
    path('best/', best_quotes, name='best_quotes'),
    path('about/', about, name="about"),
]
