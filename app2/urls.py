from django.urls import path
from app2.views import *

app_name='dictinary'

urlpatterns=[
    path('jinjaap21/',jinjaap21,name='jinjaapp21')
]