from django.db import models

class Address(models.Model):
    street_name = models.CharField(max_length=255)
    street_no = models.IntegerField()
    city = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    country = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.street_no} {self.street_name}, {self.zip_code}, {self.country}'

class Person(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Person {self.id}: {self.name} {self.last_name}; {self.email}'