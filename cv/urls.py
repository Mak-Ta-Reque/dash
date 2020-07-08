from django.urls import path
from . import views

urlpatterns = [
    path('views/', views.show_cv, name='cv_views'),
    path('add/', views.add_cv, name='cv_add')
]