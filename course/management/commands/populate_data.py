import random
import os
from faker import Faker
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from course.models import Course, Category, Chapter, Lesson, Enrollment, Curriculum, Review, Assessment

class Command(BaseCommand):
    help = 'Generate dummy data for the database'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create categories
        for _ in range(5):
            Category.objects.create(
                name=fake.word(),
                description=fake.sentence()
            )

        # Create users
        for _ in range(10):
            User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123'
            )

        users = User.objects.all()
        categories = Category.objects.all()

        # Create courses
        for _ in range(10):
            instructor = random.choice(users)
            category = random.choice(categories)

            course = Course.objects.create(
                instructor=instructor,
                category=category,
                name=fake.catch_phrase(),
                price=random.uniform(10, 100),
                subtitle=fake.sentence(),
                duration=random.randint(1, 12),
                skill_level=random.choice(['Beginner', 'Intermediate', 'Advanced']),
                language=random.choice(['En', 'Ar']),
                course_desc=fake.paragraph(nb_sentences=10),
                created_at=timezone.now(),
                updated_at=timezone.now(),
                image=self.get_random_image(),
                certification=fake.word(),
                learning_outcomes=fake.paragraph(nb_sentences=5),
            )

            # Create chapters and lessons
            self.create_dummy_chapters(course)

        # Create reviews
        for _ in range(20):
            student = random.choice(users)
            course = random.choice(Course.objects.all())
            rate = random.randint(1, 5)

            Review.objects.create(
                course=course,
                student=student,
                comment=fake.paragraph(nb_sentences=2),
                rate=rate,
                created_at=timezone.now(),
            )

        # Create assessments
        for _ in range(5):
            course = random.choice(Course.objects.all())

            Assessment.objects.create(
                course=course,
                title=fake.sentence(),
                description=fake.paragraph(nb_sentences=5),
                assessment_type=random.choice(['exam', 'quiz', 'project', 'assignment']),
                created_at=timezone.now(),
                due_date=timezone.now() + timezone.timedelta(days=random.randint(1, 30)),
            )

        self.stdout.write(self.style.SUCCESS('Dummy data generated successfully.'))

    def get_random_image(self):
        media_dir = os.path.join(os.path.dirname(__file__), '../../../media/course')
        images = [f for f in os.listdir(media_dir) if f.endswith('.jpg')]
        image_path = os.path.join('course', random.choice(images))
        return image_path

    def create_dummy_chapters(self, course):
        fake = Faker()
        num_chapters = random.randint(2, 5)
        for i in range(1, num_chapters + 1):
            chapter = Chapter.objects.create(
                course=course,
                title=fake.catch_phrase(),
                description=fake.paragraph(nb_sentences=2),
                order=i
            )
            self.create_dummy_lessons(chapter)

    def create_dummy_lessons(self, chapter):
        fake = Faker()
        num_lessons = random.randint(3, 7)
        for i in range(1, num_lessons + 1):
            lesson_type = random.choice(['text', 'video', 'pdf'])
            Lesson.objects.create(
                chapter=chapter,
                title=fake.sentence(),
                lesson_type=lesson_type,
                content=fake.paragraph(nb_sentences=3) if lesson_type == 'text' else None,
                video_file=fake.file_name(category='video') if lesson_type == 'video' else None,
            )
