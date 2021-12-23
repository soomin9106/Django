from django.urls.conf import path
from menuapp.views import first
from menuapp.views import add
from menuapp.views import artist




app_name = 'menuapp'

urlpatterns = [
    path('first/', first ,name='first'),
    path('add/',add,name='add'),
    path('artist/',artist,name='artist'),
]