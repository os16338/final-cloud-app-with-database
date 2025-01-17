# Generated by Django 3.1.3 on 2022-10-04 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0003_question_questioncontent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question',
            new_name='question_id',
        ),
        migrations.RenameField(
            model_name='submission',
            old_name='enrollment',
            new_name='enrollment_id',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='text',
        ),
        migrations.RemoveField(
            model_name='question',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='question',
            name='text',
        ),
        migrations.RemoveField(
            model_name='question',
            name='title',
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default='', max_length=35),
        ),
        migrations.AddField(
            model_name='question',
            name='gradePoint',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='question',
            name='lesson_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.lesson'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='is_correct',
            field=models.BooleanField(),
        ),
    ]
