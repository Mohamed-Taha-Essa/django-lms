# Generated by Django 4.2 on 2024-06-07 08:06

import ckeditor.fields
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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('order', models.PositiveIntegerField(verbose_name='order')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='price')),
                ('subtitle', models.TextField(max_length=1000, verbose_name='subtitle')),
                ('duration', models.IntegerField(default=100, verbose_name='duration')),
                ('skill_level', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], max_length=50, verbose_name='skill level')),
                ('language', models.CharField(choices=[('En', 'English'), ('Ar', 'Arabic')], max_length=50, verbose_name='language')),
                ('course_desc', models.TextField(max_length=30000, verbose_name='course description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('image', models.ImageField(upload_to='course', verbose_name='image')),
                ('certification', models.CharField(blank=True, max_length=255, null=True, verbose_name='certification')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses_category', to='course.category', verbose_name='category')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_instructor', to=settings.AUTH_USER_MODEL, verbose_name='instructor')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='comment')),
                ('rate', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], verbose_name='rate')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created at')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_course', to='course.course', verbose_name='course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_student', to=settings.AUTH_USER_MODEL, verbose_name='student')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('lesson_type', models.CharField(choices=[('text', 'Text'), ('video', 'Video'), ('pdf', 'PDF')], max_length=10, verbose_name='lesson type')),
                ('content', models.FileField(blank=True, null=True, upload_to='lesson/pdf/', verbose_name='content')),
                ('video_file', models.FileField(blank=True, null=True, upload_to='lesson/video/', verbose_name='video file')),
                ('duration', models.IntegerField(default=100, verbose_name='duration')),
                ('content_vid_pdf', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons_chapter', to='course.chapter', verbose_name='chapter')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrolled_at', models.DateTimeField(auto_now_add=True, verbose_name='enrolled at')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments_course', to='course.course', verbose_name='course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments_student', to=settings.AUTH_USER_MODEL, verbose_name='student')),
            ],
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('order', models.PositiveIntegerField(verbose_name='order')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curriculums_course', to='course.course', verbose_name='course')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters_course', to='course.course', verbose_name='course'),
        ),
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('assessment_type', models.CharField(choices=[('exam', 'Exam'), ('quiz', 'Quiz'), ('project', 'Project'), ('assignment', 'Assignment')], max_length=20, verbose_name='assessment type')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('due_date', models.DateTimeField(blank=True, null=True, verbose_name='due date')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assessments_course', to='course.course', verbose_name='course')),
            ],
        ),
    ]
