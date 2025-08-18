from django.shortcuts import render, get_object_or_404
from .models import Reviews


def reviews(request):
    reviews = Reviews.objects.order_by('-date')
    return render(request, 'reviews/reviews.html', {'reviews': reviews})
