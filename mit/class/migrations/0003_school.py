# Generated by Django 5.0.2 on 2024-02-26 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0002_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('address', models.IntegerField()),
            ],
        ),
    ]
