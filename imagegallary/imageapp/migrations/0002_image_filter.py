# Generated by Django 2.2.7 on 2021-01-30 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='filter',
            field=models.CharField(choices=[('all', 'ALL'), ('public', 'PUBLIC'), ('private', 'PRIVATE'), ('family', 'FAMILY'), ('friends', 'FRIENDS'), ('party', 'PARTY')], default='all', max_length=7),
        ),
    ]
