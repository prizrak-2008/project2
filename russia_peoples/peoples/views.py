from django.shortcuts import render, get_object_or_404
from .models import Nation

def home(request):
    nations = Nation.objects.all()
    return render(request, 'home.html', {'nations': nations})

def nation_detail(request, nation_id):
    nation = get_object_or_404(Nation, id=nation_id)
    return render(request, 'nation_detail.html', {'nation': nation})