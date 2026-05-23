from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('<int:nation_id>/', views.nation_detail, name='nation_detail'),
]