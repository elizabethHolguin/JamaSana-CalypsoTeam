from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import Cliente
from .models import Administrador
from .models import Vendedor
from seguridad.models import Tarjeta

from .serializers import ClienteSerializer
from .serializers import AdministradorSerializer
from .serializers import VendedorSerializer
from .serializers import UserSerializer

from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework import generics

from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from django.contrib.auth import authenticate, login
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClienteSerializer

class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AdministradorSerializer


class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VendedorSerializer

##Funciones de Login

#Get if User have active Token
#Unique Token for User
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def isActiveToken(request,user):
    active=Token.objects.filter(user=user).exists()
    data = {'active': active}
    return Response(data, status=status.HTTP_200_OK)



@api_view(['POST'])
@authentication_classes([])
@permission_classes([AllowAny])
def login(request):
    serializer = ObtainAuthToken.serializer_class(
        data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    
    try:    
        cliente = Cliente.objects.get(user=user)
        token, created = Token.objects.get_or_create(user=user) 
        data = {
            "nombre": cliente.nombre,
            "apellido": cliente.apellido,
            "username": cliente.user.username,
            "email": cliente.user.email,
            "direccion": cliente.direccion,
            "fecha_nacimiento": cliente.fecha_nacimiento,
            'Auth-token': token.key,
        }
        return Response(data, status=HTTP_200_OK)
    except:
        return Response({'error': 'User not authorized'}, status=HTTP_404_NOT_FOUND)
    
    

@api_view(['POST'])
@authentication_classes([])
@permission_classes([AllowAny])
def login_admin(request):
    
    serializer = ObtainAuthToken.serializer_class(
        data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']

    try:
        admin = Administrador.objects.get(user=user)
        token, created = Token.objects.get_or_create(user=user)
        data = {
            "nombre": admin.user.first_name,
            "apellido": admin.user.last_name,
            "username": admin.user.username,
            "email": admin.user.email,
            'Auth-token': token.key,
        }
        return Response(data, status=HTTP_200_OK)
    except:
        return Response({'error': 'User not authorized'}, status=HTTP_404_NOT_FOUND)


    

@api_view(['POST'])
@authentication_classes([])
@permission_classes([AllowAny])
def login_vendedor(request):
    
    serializer = ObtainAuthToken.serializer_class(
        data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']

    try:
        vendedor = Vendedor.objects.get(user=user)
        token, created = Token.objects.get_or_create(user=user)
        data = {
            "nombre": vendedor.user.first_name,
            "apellido": vendedor.user.last_name,
            "username": vendedor.user.username,
            "email": vendedor.user.email,
            'Auth-token': token.key,
        }
        return Response(data, status=HTTP_200_OK)
    except:
        return Response({'error': 'User not authorized'}, status=HTTP_404_NOT_FOUND)
        



##Funciones Para Registro de Usuarios

@api_view(['POST'])
@authentication_classes([])
@permission_classes([AllowAny])
def registrar(request):
    username = request.data.get("username")
    userExists=User.objects.filter(username=username).exists()
    if(userExists):
        msg={
            'error':"User already exists."
        }
        return Response(msg,status=status.HTTP_400_BAD_REQUEST)
    
    email = request.data.get("email")
    emailExists=User.objects.filter(email=email).exists()
    if(emailExists):
        msg={
            'error':"Email already exists."
        }
        return Response(msg,status=status.HTTP_400_BAD_REQUEST)
    
    password = make_password(request.data.get("password"))

    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")

    data = {
        "username": username,
        "email": email,
        "password": password,
        "first_name": first_name,
        "last_name": last_name
    }

    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        try:
            direccion = request.data.get("direccion")
            fecha = request.data.get("fecha")
            user = User.objects.get(username=username)
            tarjeta = Tarjeta.objects.get(pk=1)
            cliente = Cliente().crearCliente(user,first_name,last_name,email,direccion,fecha)
            if cliente is not None:
                data2 = {
                    "username": username,
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name
                }
                return Response(data2, status=status.HTTP_201_CREATED)
            else:
                msg={
                    'error':"Error creating user cliente in database"
                }
                return Response(msg,status=status.HTTP_400_BAD_REQUEST)
        except:
            msg={
                'error':"Error creating user cliente because of tarjeta or cliente"
            }
            return Response(msg,status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([AllowAny])
def registrar_vendedor(request):
    username = request.data.get("username")
    userExists=User.objects.filter(username=username).exists()
    if(userExists):
        msg={
            'error':"User already exists."
        }
        return Response(msg,status=status.HTTP_400_BAD_REQUEST)
    
    email = request.data.get("email")
    emailExists=User.objects.filter(email=email).exists()
    if(emailExists):
        msg={
            'error':"Email already exists."
        }
        return Response(msg,status=status.HTTP_400_BAD_REQUEST)
    
    password = make_password(request.data.get("password"))

    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")

    data = {
        "username": username,
        "email": email,
        "password": password,
        "first_name": first_name,
        "last_name": last_name
    }

    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        try:
            user = User.objects.get(username=username)
            vendedor = Vendedor().crearVendedor(user)
            if vendedor is not None:
                data2 = {
                    "username": username,
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name
                }
                return Response(data2, status=status.HTTP_201_CREATED)
            else:
                msg={
                    'error':"Error creating user vendedor in database"
                }
                return Response(msg,status=status.HTTP_400_BAD_REQUEST)
        except:
            msg={
                'error':"Error creating user vendedor because of user account"
            }
            return Response(msg,status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)





    




