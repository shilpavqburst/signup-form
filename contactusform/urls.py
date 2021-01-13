from django.urls import path
from django.views.generic.base import RedirectView
from .import views, redirect_view

urlpatterns = [

    path('register',views.contactusform_view,name="form"),
    path('', redirect_view),
    path('database',views.database_view,name="database"),
   
]
