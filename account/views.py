from django.shortcuts import get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser
from rest_framework import status

from .serializers import CustomAuthTokenSerializer, RegisterSerializer, ForgotSerializer
from .services.utils import send_activate_code, send_new_password


class LoginView(ObtainAuthToken):
    
    serializer_class = CustomAuthTokenSerializer
    

class RegisterView(APIView):
    
    def post(self,request):
        data = request.POST #(email='ofwomfw', password='fwwwg')
        serializer = RegisterSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        # serializer.validated_data #dict(data) <-----is_valid()
        user: CustomUser = serializer.save() #create()
        send_activate_code(user.activate_code, user.email)
        return Response(serializer.data)
    
class ActivateView(APIView):
    
    #http://localhost:8000/api/v1/account/activate/mowefmweok/
    def get(self, request, activate_code):
        user = get_object_or_404(CustomUser, activate_code=activate_code)
        user.is_active = True
        user.save()      
        return Response({'message': "activated"})  
    
class ForgotPasswordView(APIView):
    
    def post(self, request):
        data = request.POST
        serializer = ForgotSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        user: CustomUser = CustomUser.objects.get(email=email)
        new_password = user.password = user.generate_activation_code(10, 'qwerty12345')
        user.set_password(new_password) #lazy request
        user.save()
        send_new_password(email, new_password)
        return Response({'message': 'your new password is sent to your email'}, status=status.HTTP_200_OK)