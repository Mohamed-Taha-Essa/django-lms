from django.urls import path,include
from . views import CourseListView ,CourseDetailView

urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
]
