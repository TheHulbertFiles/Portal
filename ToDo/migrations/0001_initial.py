# Generated by Django 3.1.1 on 2021-01-30 05:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ToDo_Title', models.CharField(max_length=255)),
                ('ToDo_Date', models.DateField(blank=True, null=True)),
                ('ToDo_Time', models.TimeField(blank=True, null=True)),
                ('ToDo_Location', models.CharField(blank=True, max_length=255, null=True)),
                ('ToDo_Description', models.TextField(blank=True, null=True)),
                ('ToDo_Completed', models.BooleanField()),
                ('ToDo_Complete_Date', models.DateTimeField(blank=True, null=True)),
                ('ToDo_Author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'To-Do Items',
                'ordering': ['ToDo_Date', 'ToDo_Time'],
            },
        ),
    ]