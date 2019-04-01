# Generated by Django 2.1.7 on 2019-04-01 06:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
                ('course_code', models.CharField(max_length=16)),
                ('semester', models.CharField(max_length=3)),
                ('year', models.DateField(default=django.utils.timezone.now)),
                ('admins', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='taught_courses', to=settings.AUTH_USER_MODEL)),
                ('students', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='taken_courses', to=settings.AUTH_USER_MODEL)),
                ('teaching_assistants', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='assisted_courses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
            ],
        ),
    ]