from django.urls import path
from basic_app import views
# from learning_templates.basic_app.views import other

app_name = 'basic_app' 

urlpatterns=[
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]
