from django.urls import path
from .import views

urlpatterns = [

    path('/register',views.contactusform_view,name="form"),
    path('database',views.database_view,name="database"),
   
]
