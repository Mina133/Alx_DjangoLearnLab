# Generated by Django 5.0.6 on 2024-11-11 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Auhor',
            new_name='Author',
        ),
        migrations.RenameField(
            model_name='library',
            old_name='books',
            new_name='book',
        ),
    ]
