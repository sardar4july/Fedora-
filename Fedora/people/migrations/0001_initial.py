# Generated by Django 4.1 on 2022-09-08 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=100)),
                ('last', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'people',
            },
        ),
    ]