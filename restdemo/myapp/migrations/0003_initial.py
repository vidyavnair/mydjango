# Generated by Django 5.1.3 on 2024-11-27 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0002_delete_full_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Full_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
