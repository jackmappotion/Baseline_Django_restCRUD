from django.urls import path

from .views import StudentsListAPI, StudentsDetailAPI

app_name = "status_board"

urlpatterns = [
    path('students/', StudentsListAPI.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentsDetailAPI.as_view(), name='student-detail'),
]