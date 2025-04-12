from django.shortcuts import render,redirect

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