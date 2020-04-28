from rest_framework import serializers, viewsets
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from rest_framework.authtoken import views
class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, 
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data): 
        user = User.objects.create_user(validated_data['username'],
        validated_data['email'], 
        validated_data['password'])
        return user

    class Meta: 
        model = User
        fields = ('id', 'username', 'email', 'password')

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(user=user)