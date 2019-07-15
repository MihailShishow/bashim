# Generated by Django 2.2.2 on 2019-07-03 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abyss', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='abyssquote',
            name='approved_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='abyssquote',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]