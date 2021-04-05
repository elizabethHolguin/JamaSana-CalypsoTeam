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

from .models import TipoSuscripcion
from .models import Suscripcion
from .models import ClienteSuscripcion

from .serializers import TipoSuscripcionSerializer
from .serializers import SuscripcionSerializer
from .serializers import ClienteSuscripcionSerializer
# Create your views here.

class TipoSuscripcionViewSet(viewsets.ModelViewSet):
    queryset = TipoSuscripcion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoSuscripcionSerializer

class SuscripcionViewSet(viewsets.ModelViewSet):
    queryset = Suscripcion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SuscripcionSerializer


class ClienteSuscripcionViewSet(viewsets.ModelViewSet):
    queryset = ClienteSuscripcion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class =  ClienteSuscripcionSerializer


@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def tipoSuscripcionAll(request):
    data = TipoSuscripcion.objects.all()
    serializer = TipoSuscripcionSerializer(data, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([AllowAny])
def tipoSuscripcion(request, pk):

    if(request.method=='GET'):
        data = generics.get_object_or_404(TipoSuscripcion,id=pk)
        if data is not None:
            serializer = TipoSuscripcionSerializer(data, many=False)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'message': 'Tipo de suscripcion no existe'},status=status.HTTP_400_BAD_REQUEST)

    elif(request.method=='POST' and request.user.is_authenticated):
        serializer = TipoSuscripcionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.erros,status=status.HTTP_400_BAD_REQUEST)  

    elif(request.method=='PUT' and request.user.is_authenticated):
        data = generics.get_object_or_404(TipoSuscripcion,id=pk)
        if data is not None:
            serializer = TipoSuscripcionSerializer(data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Tipo de suscripcion no existe'},status=status.HTTP_400_BAD_REQUEST)

    elif(request.method=='DELETE' and request.user.is_authenticated):
        data = generics.get_object_or_404(TipoSuscripcion,id=pk)
        if data is not None:
            data.delete()
            msg={
                'message':'Tipo de suscripcion eliminado exitosamente'
            }
            return Response(msg,status=status.HTTP_200_OK)
        return Response({'message': 'Tipo de suscripcion no existe'},status=status.HTTP_400_BAD_REQUEST)

    else:
        msg={
            'error':'Permission Denied!'
        }
        return Response(msg,status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def suscripcionAll(request):
    data = Suscripcion.objects.all()
    serializer = SuscripcionSerializer(data, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([AllowAny])
def suscripcion(request, pk):

    if(request.method=='GET'):
        data = generics.get_object_or_404(Suscripcion,id=pk)
        if data is not None:
            serializer = SuscripcionSerializer(data, many=False)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'message': 'Suscripcion no existe'},status=status.HTTP_400_BAD_REQUEST)

    elif(request.method=='POST' and request.user.is_authenticated):
        serializer = SuscripcionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    elif(request.method=='PUT' and request.user.is_authenticated):
        data = generics.get_object_or_404(Suscripcion,id=pk)
        if data is not None:
            serializer = SuscripcionSerializer(data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Suscripcion no existe'},status=status.HTTP_400_BAD_REQUEST)

    elif(request.method=='DELETE' and request.user.is_authenticated):
        data = generics.get_object_or_404(Suscripcion,id=pk)
        if data is not None:
            data.delete()
            msg={
                'message':'Suscripcion eliminado exitosamente'
            }
            return Response(msg,status=status.HTTP_200_OK)
        return Response({'message': 'Suscripcion no existe'},status=status.HTTP_400_BAD_REQUEST)

    else:
        msg={
            'error':'Permission Denied!'
        }
        return Response(msg,status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def clienteSuscripcionAll(request):
    data = ClienteSuscripcion.objects.all()
    serializer = ClienteSuscripcionSerializer(data, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([AllowAny])
def clienteSuscripcion(request, pk):

    if(request.method=='GET'):
        data = generics.get_object_or_404(ClienteSuscripcion,id=pk)
        if data is not None:
            serializer = ClienteSuscripcionSerializer(data, many=False)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'message': 'Suscripcion de Cliente no existe'},status=status.HTTP_400_BAD_REQUEST)

    elif(request.method=='POST' and request.user.is_authenticated):
        serializer = ClienteSuscripcionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    elif(request.method=='PUT' and request.user.is_authenticated):
        data = generics.get_object_or_404(ClienteSuscripcion,id=pk)
        if data is not None:
            serializer = ClienteSuscripcionSerializer(data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Suscripcion de Cliente no existe'},status=status.HTTP_400_BAD_REQUEST)

    elif(request.method=='DELETE' and request.user.is_authenticated):
        data = generics.get_object_or_404(ClienteSuscripcion,id=pk)
        if data is not None:
            data.delete()
            msg={
                'message':'Suscripcion de Cliente eliminado exitosamente'
            }
            return Response(msg,status=status.HTTP_200_OK)
        return Response({'message': 'Pedido no existe'},status=status.HTTP_400_BAD_REQUEST)

    else:
        msg={
            'error':'Permission Denied!'
        }
        return Response(msg,status=status.HTTP_403_FORBIDDEN)