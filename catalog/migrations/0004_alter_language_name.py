# Generated by Django 3.2.7 on 2021-09-27 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20210927_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]