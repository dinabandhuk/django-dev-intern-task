from django.urls import path
from .views import student_list, student_create, student_delete, student_update, student_detail

urlpatterns = [
    path('list/', student_list, name='student_list'),
    path('new/', student_create, name='student_create'),
    path('update/<int:id>/', student_update, name='student_update'),
    path('delete/<int:id>/', student_delete, name='student_delete'),
    path('student/<int:id>/', student_detail, name = 'student_detail')
]

