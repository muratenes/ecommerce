# Generated by Django 2.1.5 on 2019-09-02 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='sub_attr',
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(default='184170', editable=False, max_length=150, verbose_name='Ürün Kodu'),
        ),
    ]