# Generated by Django 4.2.5 on 2023-09-18 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opponent', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('minutes', models.IntegerField()),
                ('goals', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('yellow_cards', models.IntegerField()),
                ('red_card', models.IntegerField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.player')),
            ],
        ),
    ]