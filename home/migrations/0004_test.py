# Generated by Django 2.2.9 on 2020-01-22 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_ttest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.BigIntegerField()),
            ],
        ),
    ]
