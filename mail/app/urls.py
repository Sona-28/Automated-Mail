from django.urls import path
from app import views

app_name = 'mailapp'

urlpatterns = [
    path('', views.home, name="home"),
    path('sendMail/', views.sendMail, name='sendMail'),
    path('upload/', views.upload, name='upload'),
    path('automated/', views.Automated, name='automated'),
    path('attach/', views.EmailAttachementView.as_view(), name='attach'),
]