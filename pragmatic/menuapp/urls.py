from django.urls.conf import path
from menuapp.views import first


app_name = 'menuapp'

urlpatterns = [
    path('first/', first ,name='first'),
]