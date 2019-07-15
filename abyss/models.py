from django.db import models
from django.utils import timezone
import difflib

# Create your models here.


class Quote(models.Model):

    _initial_approved = None

    body = models.TextField(max_length=2000)
    email = models.EmailField()
    rating = models.IntegerField(default=0)
    accordion_rating = models.IntegerField(default=0)
    post_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    approved_date = models.DateTimeField(default=timezone.now())

    def __init__(self, *args, **kwargs):
        super(Quote, self).__init__(*args, **kwargs)
        self._initial_approved = self.is_approved

    def save(self, *args, **kwargs):
        if self._initial_approved != self.is_approved:
            self.approved_date = timezone.now()
            self.rating = 0
            self.accordion_rating = 0
        super(Quote, self).save(*args, **kwargs)


def get_similar_quotes(quote_to_check, min_similarity=0.5):
    similar_quotes = []
    quotes = Quote.objects.all()
    for quote in quotes:
        if quote != quote_to_check:
            seq = difflib.SequenceMatcher(None, quote_to_check.body, quote.body)
            if seq.ratio() >= min_similarity:
                similar_quotes.append(quote)
    if not similar_quotes:
        return None
    else:
        return similar_quotes
