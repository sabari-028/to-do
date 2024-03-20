# Generated by Django 5.0.1 on 2024-03-10 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_task_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('todo', 'To Do'), ('started', 'Started'), ('complete', 'Complete'), ('archived', 'Archived'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='todo', max_length=20),
        ),
    ]
