from django.shortcuts import render
from .models import Person
from .forms import PersonForm
# Create your views here.

def person_list_view(request):
    all_people = Person.objects.all
    return render(request, 'list.html', {'all': all_people})

def create_person_view(request):
    if request.POST:
        form = PersonForm(request.POST or None)
        if form.is_valid():
            form.save()
        redirect(home)
    context = {
        'form': form
    }
    return render(request, "enter_person.html", context)
