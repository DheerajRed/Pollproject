# Generated by Django 4.1.5 on 2023-01-21 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('security', '0002_delete_registermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='userregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('bio', models.CharField(max_length=500)),
            ],
        ),
    ]
