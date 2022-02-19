from django.urls import path

from .views import get_tel_hook


urlpatterns = [
    path('get_tel_hook/', get_tel_hook, name='get_tel_hook'),
]
