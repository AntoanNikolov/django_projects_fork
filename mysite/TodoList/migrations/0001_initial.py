# Generated by Django 4.2.18 on 2025-02-20 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_summary', models.CharField(max_length=200)),
                ('task_details', models.CharField(max_length=200)),
            ],
        ),
    ]
