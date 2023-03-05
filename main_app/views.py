from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Finch, Bug
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
    id_list = finch.bugs.all().values_list('id')
    bugs_finch_doesnt_have = Bug.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', { 
        'finch': finch, 'feeding_form': feeding_form, 'bugs': bugs_finch_doesnt_have
        })

class FinchCreate(CreateView):
    model  = Finch
    fields = '__all__'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name', 'tax_subclass', 'description', 'age_days']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

def assoc_bug(request, finch_id, bug_id):
    Finch.objects.get(id=finch_id).bugs.add(bug_id)
    return redirect('detail', finch_id = finch_id)

def unassoc_bug(request, finch_id, bug_id):
    Finch.objects.get(id=finch_id).bugs.remove(bug_id)
    return redirect('detail', finch_id = finch_id)

class BugList(ListView):
    model = Bug
    template_name = 'bugs/index.html'

class BugDetail(DetailView):
    model = Bug
    template_name = 'bugs/detail.html'

class BugCreate(CreateView):
    model = Bug
    fields = ['name', 'color']

    def form_valid(self, form):
        return super().form_valid(form)

class BugUpdate(UpdateView):
    model = Bug
    fields = ['name', 'color']

class BugDelete(DeleteView):
    model = Bug
    success_url = '/bugs/'