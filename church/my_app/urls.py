from django.urls import path
from . import views

# mapping the urls

urlpatterns= [

   path('',views.Index, name='Index'),
   path('sermons/',views.sermons,name = 'sermons'),
   path('contact/',views.contact, name = 'contact'),
   path('upcoming/',views.upcoming, name = 'upcoming'),
   path('registration/',views.registration, name ='registration'),
   path('registering/',views.member, name ='member'),
   path('donations',views.donations, name ='donations'),
   path('subscription',views.subscription, name ='subscription'),
   path('aboutUs',views.aboutUs, name ='aboutUs'), 

]