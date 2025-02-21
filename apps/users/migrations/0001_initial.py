# Generated by Django 4.1.10 on 2024-03-18 16:02

from django.db import migrations, models
import uuid

from common.constants.permission_constants import RoleConstants
from users.models import password_encrypt


def insert_default_data(apps, schema_editor):
    UserModel = apps.get_model('users', 'User')
    UserModel.objects.create(id='f0dd8f71-e4ee-11ee-8c84-a8a1595801ab', email='', username='admin',
                             nick_name="系统管理员",
                             password=password_encrypt('MaxKB@123..'),
                             role=RoleConstants.ADMIN.name,
                             is_active=True)


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False,
                                        verbose_name='主键id')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='邮箱')),
                ('phone', models.CharField(default='', max_length=20, verbose_name='电话')),
                ('nick_name', models.CharField(default='', max_length=150, verbose_name='昵称')),
                ('username', models.CharField(max_length=150, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=150, verbose_name='密码')),
                ('role', models.CharField(max_length=150, verbose_name='角色')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.RunPython(insert_default_data)
    ]
