# Generated by Django 2.2.2 on 2019-07-03 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abyss', '0003_auto_20190703_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='approved_date',
            field=models.DateTimeField(),
        ),
    ]
