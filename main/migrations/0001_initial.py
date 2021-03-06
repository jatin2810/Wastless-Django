# Generated by Django 3.0.9 on 2020-08-03 17:14

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
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('image1', models.ImageField(upload_to='product_image1')),
                ('image2', models.ImageField(upload_to='product_image2')),
                ('image3', models.ImageField(upload_to='product_image3')),
                ('category', models.CharField(choices=[('book', 'book'), ('electronic', 'electronic'), ('furniture', 'furniture'), ('clothing', 'clothing'), ('sport', 'sport'), ('stationary', 'stationary'), ('daily_use', 'daily_use'), ('other', 'other')], default='book', max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
