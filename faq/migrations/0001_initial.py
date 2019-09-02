# Generated by Django 2.0 on 2019-01-14 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SSS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='baslik')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='aciklama')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Soru',
                'verbose_name_plural': 'Sorular',
            },
        ),
    ]