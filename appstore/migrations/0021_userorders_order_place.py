# Generated by Django 3.2.4 on 2021-06-18 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstore', '0020_auto_20210618_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorders',
            name='order_place',
            field=models.CharField(default='', max_length=100, verbose_name='收货地址'),
        ),
    ]