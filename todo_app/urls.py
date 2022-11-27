from django.urls import path
from .views import (HomeView, TaskItemsListView, TaskItemCreateView, TaskItemArchivedListView,
                    TaskItemUpdateView, TaskItemDeleteView, TaskItemDetailView)

app_name = "todo_app"

urlpatterns = [
    path('', HomeView.as_view(), name="index"),
    path('tasks/', TaskItemsListView.as_view(), name="tasks"),
    path('tasks/archived/', TaskItemArchivedListView.as_view(), name="tasks_archived"),
    path('tasks/create/', TaskItemCreateView.as_view(), name="task_create"),
    path('tasks/edit/<int:pk>/', TaskItemUpdateView.as_view(), name="task_edit"),
    path('tasks/delete/<int:pk>/', TaskItemDeleteView.as_view(), name="task_delete"),
    path('tasks/detail/<int:pk>/', TaskItemDetailView.as_view(), name="task_detail"),

]
