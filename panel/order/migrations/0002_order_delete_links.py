# Generated by Django 4.1.4 on 2024-09-18 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_code', models.CharField(max_length=255)),
                ('user', models.CharField(max_length=255)),
                ('chat_id', models.CharField(max_length=255)),
                ('message_id', models.CharField(max_length=255)),
                ('expiration', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Links',
        ),
    ]
