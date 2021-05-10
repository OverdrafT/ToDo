from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('task-detal/<str:pk>', views.taskDetail, name="task-detail"),
    path('task-create/', views.taskCreate, name="task-create"),
    path('task-list/', views.taskList, name="task-list"),
    path('task-update/<str:pk>', views.taskUpdate, name="task-update"),
    path('task-delete/<str:pk>', views.taskDelete, name="task-delete"),
]