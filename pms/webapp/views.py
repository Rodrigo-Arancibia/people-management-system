from django.shortcuts import render

from people.models import Person, Address


def welcome(request):
    # Use of Person model class to obtain the amount of people listed on the database.
    no_people = Person.objects.count()
    people = Person.objects.order_by('id') # By default ID's will be order ascending (otherwise, parameter '-id' will cause ID's to be orderer descending).

    no_addresses = Address.objects.count()
    addresses = Address.objects.order_by('id')

    return render(request, 'welcome.html', {'no_people': no_people, 'people': people,
                                            'no_addresses': no_addresses, 'addresses': addresses}
                  )