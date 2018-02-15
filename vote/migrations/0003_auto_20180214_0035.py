# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-13 14:35
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vote', '0002_auto_20180213_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='номер телефона')),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Голос',
                'verbose_name_plural': 'Голоса',
            },
        ),
        migrations.AlterUniqueTogether(
            name='poll',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='poll',
            name='participate',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='user',
        ),
        migrations.RenameField(
            model_name='competition',
            old_name='Type',
            new_name='comp_type',
        ),
        migrations.RenameField(
            model_name='competition',
            old_name='Creator',
            new_name='creator',
        ),
        migrations.RenameField(
            model_name='competition',
            old_name='Rules',
            new_name='rules',
        ),
        migrations.RenameField(
            model_name='competition',
            old_name='Description',
            new_name='short_description',
        ),
        migrations.RenameField(
            model_name='participate',
            old_name='Comment',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='participate',
            old_name='Content',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='competition',
            name='Survey_date',
        ),
        migrations.RemoveField(
            model_name='participate',
            name='Creator',
        ),
        migrations.RemoveField(
            model_name='participate',
            name='competition_p',
        ),
        migrations.AddField(
            model_name='competition',
            name='survey_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 18, 14, 35, 0, 630559, tzinfo=utc), verbose_name='опрос с'),
        ),
        migrations.AddField(
            model_name='participate',
            name='competition_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='competition_participates', to='vote.Competition', verbose_name='конкурс'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participate',
            name='creator',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='user_participates', to=settings.AUTH_USER_MODEL, verbose_name='автор'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Poll',
        ),
        migrations.AddField(
            model_name='vote',
            name='participate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participate_votes', to='vote.Participate', verbose_name='заявка'),
        ),
        migrations.AddField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_votes', to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('user', 'participate')]),
        ),
    ]