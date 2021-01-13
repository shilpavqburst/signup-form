from django.urls import path
from .import views

urlpatterns = [
re_path('', RedirectView.as_view(url='/register')),
    path('register',views.contactusform_view,name="form"),
    path('database',views.database_view,name="database"),
   
]
