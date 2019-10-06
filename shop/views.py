from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse


from .models import Client

def index(request):
    latest_client_list=Client.objects.order_by('-birth_date')[:5]
    context = {
            'latest_client_list' : latest_client_list,
            }
    return render(request, 'shop/index.html', context )

def detail(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return render(request, "shop/detail.html", {client : "client"})


