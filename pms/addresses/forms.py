from django.forms import ModelForm, TextInput

from people.models import Address


class AddressForm(ModelForm):
	class Meta:
		model = Address
		fields = '__all__'
		widgets = {
		'no_address': TextInput(attrs={'type': 'number'})
		}