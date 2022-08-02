from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework import serializers, exceptions
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @staticmethod
    def _validate_email(email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False

    def validate(self, attrs):
        userName = attrs.get("username")
        password = attrs.get("password")

        # if email was given instead of username:
        if self._validate_email(userName):
            try:
                # try to get user object from db by its email
                user = User.objects.get(email=userName)

                # check for password match
                if user.check_password(password):
                    print('Password matches')

                    # set 'username' attr from user object
                    attrs['username'] = user.username
                    print(attrs)

            except User.DoesNotExist:
                raise exceptions.AuthenticationFailed(
                    'No such user with provided credentials'.title())

        data = super().validate(attrs)
        return data


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=255,
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password', 'email')

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
