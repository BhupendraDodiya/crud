from django.urls import path
from . import views

urlpatterns=[
    path('',views.signup),
    path('registration/',views.registration),
    path('login/',views.login),
    path('lf/',views.login_form),
    path('table/',views.table),
    path('wel/',views.wel),
    path('update_view/<int:uid>/',views.update_view),
    path('update_form_data/',views.update_form_data),
]