# Generated by Django 2.2.11 on 2020-03-12 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medi_app2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=264)),
                ('Image', models.ImageField(blank=True, upload_to='blog')),
                ('Content', models.TextField()),
                ('Published_Date', models.DateTimeField(auto_now=True)),
                ('View_Count', models.PositiveIntegerField(default=0)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medi_app2.Category')),
            ],
        ),
    ]