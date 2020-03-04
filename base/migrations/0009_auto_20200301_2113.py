# Generated by Django 3.0.2 on 2020-03-01 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20200301_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.CharField(default='abc', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='img',
            field=models.FileField(default='abc.jpeg', upload_to='profilepic'),
        ),
    ]
