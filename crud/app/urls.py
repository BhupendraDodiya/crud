from django.urls import path
from . import views

urlpatterns=[
    path('',views.signup),
    path('registration/',views.registration),
    path('login/',views.login),
    path('lf/',views.login_form),
    path('table/',views.table),
]