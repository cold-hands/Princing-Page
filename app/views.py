from django.shortcuts import render, redirect
from app.forms import PlanosForm
from app.models import Planos

# Create your views here.
def home(request):
    data = {}
    data['db'] = Planos.objects.all()
    return render(request, 'index.html', data)

def table(request):
    data = {}
    data['db'] = Planos.objects.all()
    return render(request, 'index2.html', data)

def form(request):
    data = {}
    data['form'] = PlanosForm()
    return render(request, 'form.html', data)

def create(request):
    form = PlanosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Planos.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Planos.objects.get(pk=pk)
    data['form'] = PlanosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Planos.objects.get(pk=pk)
    form = PlanosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('home')

def delete(request, pk):
    db = Planos.objects.get(pk=pk)
    db.delete()
    return redirect('home')