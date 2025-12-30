from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('map/<int:id>/', views.map, name='map'),
    path('update/', views.UpdateLocationView.as_view(), name='update_location'),
    path('last/<str:imei>/', views.LastLocationView.as_view(), name='last_location'),
    path('last_id/<str:imei>/', views.LastLocationIdView.as_view(), name='last_location_id'),
]