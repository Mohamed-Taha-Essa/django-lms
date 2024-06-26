from django.shortcuts import render
from django.db.models import Count

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import Course ,Review



class CourseListView(ListView):
    model = Course
    template_name = 'course/course_list.html'
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'course/course_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chapters'] = self.object.chapters_course.prefetch_related('lessons_chapter').all()
        review_statistics = Review.objects.filter(course=self.object).values('rate').annotate(count=Count('id'))
        context['review_statistics'] = review_statistics

          # Check if the instructor is an instructor and include in the context
        if self.object.instructor.profile.is_instructor:
            context['instructor'] = self.object.instructor
        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['num_lessons'] = self.object.chapters_course.all().aggregate(num_lessons=Count('lessons_chapter'))['num_lessons']

    #     return context