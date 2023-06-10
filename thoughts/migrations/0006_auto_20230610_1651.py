# Generated by Django 2.2.24 on 2023-06-10 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thoughts', '0005_auto_20230609_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('0', 'Visible'), ('1', 'Pending'), ('2', 'Deleted by Author'), ('3', 'Delted by Mods')], default='2', max_length=1),
        ),
        migrations.AlterField(
            model_name='thought',
            name='status',
            field=models.CharField(choices=[('0', 'Visible'), ('1', 'Pending'), ('2', 'Deleted by Author'), ('3', 'Delted by Mods')], default='2', max_length=1),
        ),
    ]
