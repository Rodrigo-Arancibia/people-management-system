# Generated by Django 3.0.8 on 2020-07-18 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255)),
                ('street_no', models.IntegerField()),
                ('zip_code', models.IntegerField()),
                ('country', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.Address'),
        ),
    ]
