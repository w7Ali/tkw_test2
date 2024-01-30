from django.shortcuts import render

def task2(request):
    person = {'name': 'Ram', 'age': 21, 'gender': 'Male'}
    printvar = 'name'
    return render(request, 'home.html', {'person': person, 'printvar': printvar})
