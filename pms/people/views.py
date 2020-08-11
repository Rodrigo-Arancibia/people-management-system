from django.shortcuts import render, get_object_or_404, redirect

from people.forms import PersonForm
from people.models import Person


def detail_person(request, id):
    person = get_object_or_404(Person, pk=id)
    return render(request, 'people/detail_person.html', {'person': person})


def new_person(request):
    # If the petition was GET type it means the client is requiring to add a new Person object. And it comes from the link in 'people/templates/people/new_person.html'.
    # But if the petition was POST type it means the client is submitting the info on the form.
    if request.method == 'POST': # Handles the POST type request.
        personForm = PersonForm(request.POST) # All the info in the form is stored in the 'request' object.
        if personForm.is_valid():
            personForm.save() # Saves the info from the form to the database.
            return redirect('index') # Redirects to home page ('index')
    else: # Handles the GET type request.
        personForm = PersonForm()
        return render(request, 'people/new_person.html', {'formPerson': personForm})


def edit_person(request, id):
    person = get_object_or_404(Person, pk=id)
    # If the petition was GET type it means the client is requiring to add a new Person object. And it comes from the link in 'people/templates/people/edit_person.html'.
    # But if the petition was POST type it means the client is submitting the info on the form.
    if request.method == 'POST': # Handles the POST type request.
        personForm = PersonForm(request.POST, instance=person) # All the info in the form is stored in the 'request' object.
        if personForm.is_valid():
            personForm.save() # Updates the info on the database. More info about the 'save()' method here: https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/
            return redirect('index') # Redirects to home page ('index')
    else: # Handles the GET type request.
        personForm = PersonForm(instance=person)
        return render(request, 'people/edit_person.html', {'formPerson': personForm})


def delete_person(request, id):
    person = get_object_or_404(Person, pk=id)
    if person:
        person.delete()
    return redirect('index')