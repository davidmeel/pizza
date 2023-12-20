# Generated by Django 5.0 on 2023-12-18 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='menu')),
                ('title', models.CharField(max_length=50)),
                ('info', models.CharField(max_length=64)),
                ('price', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'menu',
                'verbose_name_plural': 'menues',
            },
        ),
    ]
