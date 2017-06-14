# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-06-14 08:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('employee_id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('is_dashboard', models.BooleanField(default=False)),
                ('is_side_menu', models.BooleanField(default=False)),
                ('is_subcategory', models.BooleanField(default=False)),
                ('type', models.CharField(blank=True, choices=[('list', 'list'), ('News', 'News'), ('content_list', 'content_list'), ('gallery', 'gallery')], max_length=20, null=True)),
                ('logo', models.CharField(default='', max_length=254)),
                ('is_deleted', models.BooleanField(default=False)),
                ('emp_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=250)),
                ('subtitle', models.CharField(max_length=250)),
                ('logo', models.CharField(default='', max_length=254)),
                ('link', models.CharField(default='', max_length=254)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jaincontent.Category')),
                ('emp_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(blank=True, choices=[('list', 'list'), ('News', 'News'), ('content_list', 'content_list'), ('gallery', 'gallery')], max_length=20, null=True)),
                ('logo', models.CharField(default='', max_length=254)),
                ('is_deleted', models.BooleanField(default=False)),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jaincontent.Category')),
                ('emp_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='sub_category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jaincontent.SubCategory'),
        ),
    ]
