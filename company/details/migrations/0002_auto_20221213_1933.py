# Generated by Django 3.2 on 2022-12-13 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': '2. Company'},
        ),
        migrations.AlterModelOptions(
            name='industrytype',
            options={'verbose_name_plural': '1. IndustryType'},
        ),
        migrations.RenameField(
            model_name='industrytype',
            old_name='name',
            new_name='industryname',
        ),
    ]
