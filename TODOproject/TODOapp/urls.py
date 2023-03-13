from . import views
from django.urls import path

app_name = 'TODOapp'

urlpatterns = [

    # .....url creations based on functions ............

    path("", views.Home,name="Home"),
    path('Details',views.Details,name='Details.html'),
    path('Delete/<int:taskid>/',views.Delete,name='Delete'),
    path('update/<int:id>/', views.update, name='update'),


    # .......url creations based on class .............

    path('cbvHome/',views.TaskListView.as_view(),name='cbvHome'),
    path('cbvdetail/<int:pk>/',views.TaskDetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvdelete'),
]
