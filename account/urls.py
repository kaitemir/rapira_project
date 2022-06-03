from django.urls import path

from .views import ActivateView, LoginView, RegisterView, ForgotPasswordView

#http://127.0.0.1:8000/api/v1/account --->urlpatterns
urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('activate/<str:activate_code>/', ActivateView.as_view()),
    path('forgot_password/', ForgotPasswordView.as_view())
]

#TODO Forgot PAssword (account)
#TODO SHopping Cart (auto-create)