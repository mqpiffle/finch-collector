from django.shortcuts import render

finches = [
    {'name': 'Tweetz', 'tax_subclass': 'Mycerobas', 'age_days': 210},
    {'name': 'Scooter', 'tax_subclass': 'Procardeulis', 'age_days': 55}
]
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', { "finches": finches })