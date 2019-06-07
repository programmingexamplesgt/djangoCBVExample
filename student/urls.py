from django.urls import path
from .views import (
    CreateStudent, ListStudent, UpdateStudent, DetailStudent)


urlpatterns = [
    path('create/', CreateStudent.as_view(), name='create-student'),
    path('list/', ListStudent.as_view(), name='list-student'),
    path('update/<pk>/', UpdateStudent.as_view(), name='update-student'),
    path('<pk>/', DetailStudent.as_view(), name='detail-student'),
]
