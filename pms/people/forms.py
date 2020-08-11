# Personalize the elements to show in the form.
#

from django.forms import ModelForm, EmailInput

from people.models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person # Use of Model Class.
        fields = '__all__' # Indicates which class fields we are going to use. The use of '__all__' indicates we are using all the class fields.
        # Indicates the Person form field type. More info at: https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }