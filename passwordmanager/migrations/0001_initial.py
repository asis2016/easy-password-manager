# Generated by Django 5.0 on 2023-12-25 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('username', models.TextField()),
                ('password', models.TextField()),
                ('url', models.TextField()),
                ('datestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
