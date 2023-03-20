from django.http import HttpResponse
from django.shortcuts import render
from rewards.models import Rewards, Leagues


def gw_rewards(request):
    data = Rewards.objects.select_related('league').all()
    percentage = data[0]
    print(data)
    context = {'data': data}
    # rewards = Rewards.objects.all()
    # leagues = Leagues.objects.all()
    # return render(request, 'index.html', {'rewards': rewards},)
    return render(request, 'index.html', context)
