from django.shortcuts import render
from django.http import HttpResponse
						


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all administrators
    administrators = administrator.objects.order_by('-hire_date')

    # Get MVP
    mvp_administrators = administrator.objects.all().filter(is_mvp=True)

    context = {
        'administrators': administrators,
        'mvp_administrators': mvp_administrators
    }

    return render(request, 'pages/about.html', context)