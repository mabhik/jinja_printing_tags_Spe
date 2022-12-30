from django.urls import path
from app1.views import *

app_name="project7"

urlpatterns=[
    path('jinja/',jinja,name='jinja'),
    path('jinja2/',jinja2,name='jinja2'),
    path('jinja12/',jinja12,name='jinja12'),
    path('one1/',one1,name='one1')
]