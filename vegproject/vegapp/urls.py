from django.urls import path

from . import views



urlpatterns = [
    
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    

    path('response/', views.responseform, name='responseform' ),
    path('thankyou/', views.responseform, name='responseform'),   
]
   
