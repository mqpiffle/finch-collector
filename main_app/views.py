from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch
from .forms import FeedingForm

# finches = [
#     {'name': 'Tweetz', 'tax_subclass': 'Mycerobas', 'description': 'cute little thing', 'age_days': 210},
#     {'name': 'Scooter', 'tax_subclass': 'Procardeulis', 'description': 'monster', 'age_days': 55}
# ]
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', { "finches": finches })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', { 
        'finch': finch, 'feeding_form': feeding_form 
        })

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
    model  = Finch
    fields = '__all__'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name', 'description', 'age_days']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'