# Generated by Django 4.2.6 on 2024-02-12 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_poll_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectionCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='poll',
            name='Category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='polls.electioncategories'),
            preserve_default=False,
        ),
    ]
