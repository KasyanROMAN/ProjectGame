from django.shortcuts import render,redirect
from django.http import HttpResponse
from product.forms import GameForm
from product.models import Game

# Create your views here.

def index(request):
    games = Game.objects.all()
    return render(request,'index.html',{'games':games})
def create_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        form.save()
        return redirect('/')
    else:
        form = GameForm()
    return render(request, 'create.html', {'form':form})
def delete_game(request,id_game):
    try:
        game = Game.objects.get(id = id_game)
        game.delete()
        return redirect('/')
    except Game.DoesNotExist:
        return HttpResponse('Error')
def detail(request,id_product):
    game = Game.objects.get(id =id_product)
    return render(request,'detail.html',{'game':game})