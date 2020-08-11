from django.shortcuts import render, get_object_or_404, redirect

from addresses.forms import AddressForm
from people.models import Address


def detail_address(request, id):
    address = get_object_or_404(Address, pk=id)
    return render(request, 'addresses/detail_address.html', {'address': address})


def new_address(request):
    # If the petition was GET type it means the client is requiring to add a new Address object. And it comes from the link in 'addresses/templates/addresses/new_address.html'.
    # But if the petition was POST type it means the client is submitting the info on the form.
    if request.method == 'POST': # Handles the POST type request.
        addressForm = AddressForm(request.POST) # All the info in the form is stored in the 'request' object.
        if addressForm.is_valid():
            addressForm.save() # Saves the info from the form to the database.
            return redirect('index') # Redirects to home page ('index')
    else: # Handles the GET type request.
        addressForm = AddressForm()
        return render(request, 'addresses/new_address.html', {'formAddress': addressForm})


def edit_address(request, id):
    address = get_object_or_404(Address, pk=id)
    # If the petition was GET type it means the client is requiring to add a new Person object. And it comes from the link in 'people/templates/people/edit_person.html'.
    # But if the petition was POST type it means the client is submitting the info on the form.
    if request.method == 'POST':  # Handles the POST type request.
        addressForm = AddressForm(request.POST,
                                instance=address)  # All the info in the form is stored in the 'request' object.
        if addressForm.is_valid():
            addressForm.save()  # Updates the info on the database. More info about the 'save()' method here: https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/
            return redirect('index')  # Redirects to home page ('index')
    else:  # Handles the GET type request.
        addressForm = AddressForm(instance=address)
        return render(request, 'addresses/edit_address.html', {'formAddress': addressForm})


def delete_address(request, id):
    address = get_object_or_404(Address, pk=id)
    if address:
        address.delete()
    return redirect('index')