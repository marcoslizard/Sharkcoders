from django.urls import path
from.import views



urlpatterns = [
    path('',views.index, name='index'),
    path('delete/<int:pk>/', views.deleteTask, name='delete-task'),
    path('complete/<int:pk>/',views.completeTask, name='complete-task'),
]