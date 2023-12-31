# Generated by Django 5.0 on 2023-12-24 15:38

import ckeditor.fields
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(upload_to='author_images/')),
                ('designation', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=350, null=True)),
                ('lesson', models.PositiveIntegerField(default=0)),
                ('duration', models.PositiveIntegerField(default=0)),
                ('skill_level', models.CharField(choices=[('Advanced', 'Advanced'), ('Intermediate', 'Intermediate'), ('Basic', 'Basic')], default='Basic', max_length=50)),
                ('language', models.CharField(choices=[('Bangla', 'Bangla'), ('English', 'English')], default='Bangla', max_length=20)),
                ('course_details', ckeditor.fields.RichTextField()),
                ('banner', models.ImageField(upload_to='courses_banner/')),
                ('course_files', models.FileField(blank=True, null=True, upload_to='course_files/')),
                ('price', models.PositiveIntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_author', to='lms.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_category', to='lms.category')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=20)),
                ('transaction_id', models.CharField(max_length=50, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(choices=[('CSE', 'Computer Science and Engineering'), ('EEE', 'Electrical and Electronics Engineering'), ('CE', 'Civil Engineering'), ('ENGLISH', 'English'), ('BBA', 'Bachelor of Business Administration'), ('MECHANICAL', 'Mechanical Engineering')], max_length=50)),
                ('semester', models.CharField(choices=[('1', 'Semester 1'), ('2', 'Semester 2'), ('3', 'Semester 3'), ('4', 'Semester 4'), ('5', 'Semester 5'), ('6', 'Semester 6'), ('7', 'Semester 7'), ('8', 'Semester 8')], max_length=20)),
                ('approved', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('is_preview', models.BooleanField(default=False)),
                ('video_file', models.FileField(upload_to='course_videos/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='lms.course')),
            ],
        ),
    ]
