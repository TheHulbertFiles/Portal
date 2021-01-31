# Generated by Django 3.1.1 on 2021-01-30 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Demo_Name', models.CharField(max_length=255)),
                ('Demo_Image', models.ImageField(upload_to='images/')),
                ('Demo_Version', models.CharField(max_length=5)),
                ('Demo_Description', models.TextField()),
                ('Demo_Date_Developed', models.DateField(blank=True, null=True)),
                ('Demo_Update_Date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Demos',
                'ordering': ['Demo_Name'],
            },
        ),
    ]