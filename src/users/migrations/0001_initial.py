# Generated by Django 5.0 on 2024-02-08 01:35

import django.db.models.deletion
import users.models.userbase
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('model', models.CharField(max_length=255)),
                ('status', models.CharField(default='processing', max_length=255)),
                ('document', models.FileField(blank=True, null=True, upload_to='')),
            ],
            options={
                'ordering': ['-is_active', '-id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GeneralSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_for_month', models.PositiveBigIntegerField(default=1000)),
                ('price_for_trimonthly', models.PositiveBigIntegerField(default=2500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GlobalNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('msg', models.TextField(default='')),
                ('trigger_type', models.CharField(choices=[('all', 'All'), ('subscribed', 'Subscribed'), ('agents', 'Agents')], max_length=20)),
                ('is_processed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='VerificationCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, editable=False, max_length=6, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('is_email_sent', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('expiration_time', models.DateTimeField(blank=True, null=True)),
                ('otp_for', models.CharField(default='email_verification', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('provider', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('provider_uuid', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('family_name', models.CharField(blank=True, max_length=150)),
                ('given_name', models.CharField(max_length=150)),
                ('phone_number', models.CharField(blank=True, default='', max_length=15)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to=users.models.userbase.image_directory_path)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_agent', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('referred_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddConstraint(
            model_name='verificationcode',
            constraint=models.UniqueConstraint(fields=('code', 'email'), name='verification_unique_constraints'),
        ),
    ]
