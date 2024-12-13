from django.urls import path
from myapp.views import person,single_details
urlpatterns = [
    # path('index_display/',index_display,name='index'),
    path('person/',person,name='person'),
    path('single_details/<int:pk>',single_details,name='single_details')
]