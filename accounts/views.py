from django.contrib.auth import get_user_model, authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


User = get_user_model()

# Create your views here.
class Login(APIView):
    queryset = User.objects.all()
    
    def post(self, request):
        if user := authenticate(username=request.data['username'], password=request.data['password']):
            token = Token.objects.get_or_create(user=user)[0]

            return Response({'token': token.key})

        return Response({'message': "Unauthorized"})
