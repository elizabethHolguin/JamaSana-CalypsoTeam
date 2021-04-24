from django.shortcuts import render
from rest_framework import viewsets, permissions

from django.http import JsonResponse
from rest_framework.response import Response

from rest_framework import status
from rest_framework import generics

from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from .models import Configuracion
from .models import Perfil
from .models import PerfilE

from .serializers import ConfiguracionSerializer
from .serializers import PerfilSerializer
from .serializers import PerfilESerializer
# Create your views here.

class ConfiguracionViewSet(viewsets.ModelViewSet):
    queryset = Configuracion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ConfiguracionSerializer

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PerfilSerializer

class PerfilEViewSet(viewsets.ModelViewSet):
    queryset = PerfilE.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PerfilESerializer

@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def configuracionAll(request):
    data = Configuracion.objects.all()
    serializer = ConfiguracionSerializer(data, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([AllowAny])
def configuracion(request, pk):

    if(request.method=='GET'):
        data = generics.get_object_or_404(Configuracion,id=pk)
        if data is not None:
            serializer = ConfiguracionSerializer(data, many=False)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'message': 'Configuracion no existe'},status=status.HTTP_400_BAD_REQUEST)

    elif(request.method=='POST' and request.user.is_authenticated):
        serializer = ConfiguracionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    elif(request.method=='PUT' and request.user.is_authenticated):
        data = generics.get_object_or_404(Configuracion,id=pk)
        if data is not None:
            serializer = ConfiguracionSerializer(data, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Configuracion no existe'},status=status.HTTP_400_BAD_REQUEST)

    elif(request.method=='DELETE' and request.user.is_authenticated):
        data = generics.get_object_or_404(Configuracion,id=pk)
        if data is not None:
            data.delete()
            msg={
                'message':'Configuracion eliminado exitosamente'
            }
            return Response(msg,status=status.HTTP_200_OK)
        return Response({'message': 'Configuracion no existe'},status=status.HTTP_400_BAD_REQUEST)

    else:
        msg={
            'error':'Permission Denied!'
        }
        return Response(msg,status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def perfilAll(request):
    data = Perfil.objects.all()
    serializer = PerfilSerializer(data, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([AllowAny])
def perfil(request, pk):

    if(request.method=='GET'):
        data = generics.get_object_or_404(Perfil,id=pk)
        if data is not None:
            serializer = PerfilSerializer(data, many=False)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'message': 'Perfil no existe'},status=status.HTTP_400_BAD_REQUEST)

    elif(request.method=='POST' and request.user.is_authenticated):
        serializer = PerfilSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    elif(request.method=='PUT' and request.user.is_authenticated):
        data = generics.get_object_or_404(Perfil,id=pk)
        if data is not None:
            serializer = PerfilSerializer(data, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Perfil no existe'},status=status.HTTP_400_BAD_REQUEST)

    elif(request.method=='DELETE' and request.user.is_authenticated):
        data = generics.get_object_or_404(Perfil,id=pk)
        if data is not None:
            data.delete()
            msg={
                'message':'Perfil eliminado exitosamente'
            }
            return Response(msg,status=status.HTTP_200_OK)
        return Response({'message': 'Perfil no existe'},status=status.HTTP_400_BAD_REQUEST)

    else:
        msg={
            'error':'Permission Denied!'
        }
        return Response(msg,status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def perfilEAll(request):
    data = PerfilE.objects.all()
    serializer = PerfilESerializer(data, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
