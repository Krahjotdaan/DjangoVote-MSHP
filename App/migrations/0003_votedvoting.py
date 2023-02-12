# Generated by Django 4.1.5 on 2023-02-08 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0002_votefact_votevariant_remove_answer_users_voting_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VotedVoting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('voting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.voting')),
            ],
        ),
    ]
