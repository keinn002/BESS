# Generated by Django 4.1.1 on 2022-10-21 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(max_length=500, null=True)),
                ('image', models.ImageField(upload_to='announcement-Images')),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]