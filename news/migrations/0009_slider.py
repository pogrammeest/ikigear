# Generated by Django 3.0.4 on 2020-04-01 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20190930_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.CharField(db_index=True, max_length=200)),
                ('url', models.CharField(db_index=True, max_length=200)),
            ],
        ),
    ]
