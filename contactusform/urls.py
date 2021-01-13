from django.urls import path
from django.urls import re_path
from .import views

urlpatterns = [

    path('register',views.contactusform_view,name="form"),
    re_path('', RedirectView.as_view(url='/register')),
    path('database',views.database_view,name="database"),
   
]
