from django.urls import path
from django.views.generic.base import RedirectView
from .import views

urlpatterns = [

    path('register',views.contactusform_view,name="form"),
    path('',views.redirect_view),
    path('database',views.database_view,name="database"),
    path('saveuser',views.saveuser_view,name="saveuser"),
   
]
