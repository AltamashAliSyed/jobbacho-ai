# So i just making a separate template folder directly not on detector folder thats why i have to put this
# 'DIRS': [BASE_DIR/'templates'], in settings.py  at line 58 

from django.urls import path
from . import views
urlpatterns = [
    path('',views.detector,name="detector")
]

