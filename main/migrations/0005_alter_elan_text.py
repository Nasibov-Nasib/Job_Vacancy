# Generated by Django 4.2.2 on 2023-06-20 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_elan_apply_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elan',
            name='text',
            field=models.TextField(max_length=500, null=True),
        ),
    ]