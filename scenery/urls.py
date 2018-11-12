from django.urls import path
from . import views

app_name = 'scenery'

urlpatterns = [
    path('', views.main_view, name='main_view')
]
