from django.urls import path
from django.urls import include
from AbhiruchiWebsite import views

urlpatterns = [
    path('', views.Home),
    path('DB',views.DBI),
]
