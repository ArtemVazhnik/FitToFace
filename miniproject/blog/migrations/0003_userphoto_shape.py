# Generated by Django 3.2 on 2021-05-06 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_userphoto_shape'),
    ]

    operations = [
        migrations.AddField(
            model_name='userphoto',
            name='shape',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.shape'),
            preserve_default=False,
        ),
    ]
