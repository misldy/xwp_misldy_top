from django.urls import path
from . import views

app_name = 'usermgt'

urlpatterns=[
    path('login/', views.LoginViwe.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('edit/', views.UserEditView.as_view(), name="edit"),
]