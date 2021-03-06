# Generated by Django 2.0.1 on 2018-02-06 12:24

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='ask',
            fields=[
                ('stories_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Stories')),
            ],
            bases=('app.stories',),
        ),
        migrations.CreateModel(
            name='job',
            fields=[
                ('stories_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Stories')),
            ],
            bases=('app.stories',),
        ),
        migrations.CreateModel(
            name='new',
            fields=[
                ('stories_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Stories')),
            ],
            bases=('app.stories',),
        ),
        migrations.CreateModel(
            name='show',
            fields=[
                ('stories_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.Stories')),
            ],
            bases=('app.stories',),
        ),
    ]
