from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.utils import timezone

# Define choices using tuples instead of dictionaries
SKILLLEVEL = [
    ('Beginner', _('Beginner')),
    ('Intermediate', _('Intermediate')),
    ('Advanced', _('Advanced')),
]

LANGUAGE = [
    ('En', _('English')),
    ('Ar', _('Arabic'))
]

class Course(models.Model):
    instructor = models.ForeignKey(User, related_name='course_instructor', on_delete=models.CASCADE, verbose_name=_("instructor"))
    category = models.ForeignKey('Category', related_name='courses_category', on_delete=models.CASCADE, verbose_name=_("category"))

    name = models.CharField(_("name"), max_length=50)
    price = models.DecimalField(_("price"), max_digits=5, decimal_places=2)
    subtitle = models.TextField(_("subtitle"), max_length=1000)
    duration = models.IntegerField(_("duration"))
    skill_level = models.CharField(_("skill level"), max_length=50, choices=SKILLLEVEL)
    language = models.CharField(_("language"), max_length=50, choices=LANGUAGE)
    course_desc = models.TextField(_("course description"), max_length=30000)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
   
    certification = models.CharField(_("certification"), max_length=255, blank=True, null=True)
    learning_outcomes = models.TextField(_("learning outcomes"), blank=True, null=True)
  
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(_("name"), max_length=255)
    description = models.TextField(_("description"), blank=True, null=True)

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(User, related_name='enrollments_student', on_delete=models.CASCADE, verbose_name=_("student"))
    course = models.ForeignKey(Course, related_name='enrollments_course', on_delete=models.CASCADE, verbose_name=_("course"))
    enrolled_at = models.DateTimeField(_("enrolled at"), auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.name}"

class Curriculum(models.Model):
    course = models.ForeignKey(Course, related_name='curriculums_course', on_delete=models.CASCADE, verbose_name=_("course"))
    title = models.CharField(_("title"), max_length=255)
    description = models.TextField(_("description"), blank=True, null=True)
    order = models.PositiveIntegerField(_("order"))

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class Review(models.Model):
    course = models.ForeignKey(Course, related_name='reviews_course', on_delete=models.CASCADE, verbose_name=_("course"))
    student = models.ForeignKey(User, related_name='reviews_student', on_delete=models.CASCADE, verbose_name=_("student"))
    comment = models.TextField(_("comment"), blank=True, null=True)
    rate = models.IntegerField(_("rate"), choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(_("created at"), default=timezone.now)

    def __str__(self):
        return f"{self.student.username} - {self.course.title} - {self.rate}"

class Assessment(models.Model):
    ASSESSMENT_TYPES = (
        ('exam', _('Exam')),
        ('quiz', _('Quiz')),
        ('project', _('Project')),
        ('assignment', _('Assignment')),
    )

    course = models.ForeignKey(Course, related_name='assessments_course', on_delete=models.CASCADE, verbose_name=_("course"))
    title = models.CharField(_("title"), max_length=255)
    description = models.TextField(_("description"), blank=True, null=True)
    assessment_type = models.CharField(_("assessment type"), max_length=20, choices=ASSESSMENT_TYPES)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    due_date = models.DateTimeField(_("due date"), blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.course.title}"
