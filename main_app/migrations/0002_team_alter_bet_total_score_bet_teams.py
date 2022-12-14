# Generated by Django 4.1.1 on 2022-09-19 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='bet',
            name='total_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bet',
            name='teams',
            field=models.ManyToManyField(to='main_app.team'),
        ),
    ]
