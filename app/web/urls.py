from django.urls import path
from .views.IndexView import ViewIndex

app_name = 'web'

urlpatterns = [
    path('', ViewIndex.as_view(), name='index'),
]
