# Generated by Django 2.1.7 on 2019-03-08 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='vegetables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('images', models.FileField(blank=True, null=True, upload_to='static/crops/images')),
                ('description', models.TextField(max_length=200)),
                ('season', models.CharField(choices=[('Spring', 'Spring'), ('Summer', 'Summer'), ('Autumn', 'Autumn'), ('Winter', 'Winter')], default='Summer', max_length=40)),
                ('success_ratio', models.CharField(max_length=3)),
            ],
        ),
        migrations.AddField(
            model_name='crops',
            name='price_range',
            field=models.CharField(default='', max_length=50),
        ),
    ]
