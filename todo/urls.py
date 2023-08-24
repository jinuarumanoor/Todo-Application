from django.urls import path
from .import views
urlpatterns = [
    #Add Task
    path('addtask/',views.addTask,name='addTask'),
    #mark as done
    path('mark_as_done/<int:pk>/',views.mark_as_done,name='mark_as_done'),
    #mark as undone
    path('mark_as_Undone/<int:pk>/',views.mark_as_Undone,name='mark_as_Undone'),
    #Edit Task
    path('editTask/<int:pk>/',views.edit_task,name='edit_task'),
    #Delete Task
    path('deleteTask/<int:pk>/',views.delete_task,name='delete_task'),

]
