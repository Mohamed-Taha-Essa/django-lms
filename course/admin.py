from django.contrib import admin


from .models import Category, Course, Enrollment, Review, Curriculum, Assessment

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Review)
admin.site.register(Curriculum)
admin.site.register(Assessment)
