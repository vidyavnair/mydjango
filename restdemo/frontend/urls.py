from django.urls import path
from myapp.views import person
urlpatterns = [
    
    path('person/',person,name='person'),]