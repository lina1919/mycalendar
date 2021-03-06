# Generated by Django 4.0 on 2022-01-29 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jymap', '0002_event_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jymap.event')),
            ],
        ),
    ]
