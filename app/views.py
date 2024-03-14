from django.shortcuts import render,redirect
from .models import Lego, Figure
from .forms import LegoForm, FigureForm, LegoFormCaptcha, SearchForm
from django.forms import modelformset_factory

def home(request):
    figures = Figure.objects.all()
    legos = Lego.objects.all()
    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            figures = Figure.objects.filter(name__icontains=name)
            legos = Lego.objects.filter(name__icontains=name)
            return render(request, 'home.html', {'form': form,'figures': figures,'legos': legos})
    return render(request, 'home.html', {'form': form,'figures': figures,'legos': legos})

def create_lego(request):
    formset = modelformset_factory(Lego, form=LegoForm, extra=1)
    if request.method == 'POST':
        formset = formset(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('home')
    return render(request, 'create_lego.html', {'formset': formset})

def create_figure(request):
    formset = modelformset_factory(Figure, form=FigureForm, extra=1)
    if request.method == 'POST':
        formset = formset(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('home')
    return render(request, 'create_figure.html', {'formset': formset})

def create(request):
    form = LegoFormCaptcha()
    if request.method == 'POST':
        form = LegoFormCaptcha(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'create.html', {'form': form})


