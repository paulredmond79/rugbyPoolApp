from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('series/', views.series_list, name='series_list'),
    path('series/<int:series_id>/', views.series_detail, name='series_details'),
]