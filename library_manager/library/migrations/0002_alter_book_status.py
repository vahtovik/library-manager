# Generated by Django 5.0.7 on 2024-07-24 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('в наличии', 'в наличии'), ('выдана', 'выдана')], default='available', max_length=10),
        ),
    ]