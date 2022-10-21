
from django.urls import path
from website.views import *

urlpatterns = [
    path('',index_home),
    path('contact',contact_view),
    path('about',about_view)

]
