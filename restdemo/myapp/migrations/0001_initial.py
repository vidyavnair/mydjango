# Generated by Django 5.1.3 on 2024-11-16 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Full_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('pin', models.IntegerField()),
            ],
        ),
    ]