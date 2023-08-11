# urls.py
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('add_student/', views.add_student, name='add_student'),
    path('student_list/',views.student_list,name='student_list'),
    path('edit_student/<int:pk>',views.edit_student,name='edit_student'),
    path('delete_student/<int:pk>/',views.delete_student,name='delete_student'),
    path('student_detail/<int:pk>',views.student_detail,name="student_detail"),


    path('add_unit/', views.add_unit, name='add_unit'),
    path('unit_list/',views.unit_list,name='unit_list'),
    path('edit_unit/<int:pk>',views.edit_unit,name='edit_unit'),
    path('delete_unit/<int:pk>/',views.delete_unit,name='delete_unit'),

    path('add_course/', views.add_course, name='add_course'),
    path('course_list/',views.course_list,name='course_list'),
    path('edit_course/<int:pk>',views.edit_course,name='edit_course'),
    path('delete_course/<int:pk>/',views.delete_course,name='delete_course'),


    path('add_marks/<int:pk>', views.add_marks, name='add_marks'),
    path('marks_list/',views.marks_list,name='marks_list'),
    path('edit_marks/<int:pk>',views.edit_marks,name='edit_marks'),
    path('delete_marks/<int:pk>/',views.delete_marks,name='delete_marks'),
    path('enrolled_list/',views.enrolled_list,name='enrolled_list'),
    path('enroll/<int:pk>',views.enroll,name='enroll'),

    path('toggle_enrollment/', views.toggle_enrollment, name='toggle_enrollment'),
]
