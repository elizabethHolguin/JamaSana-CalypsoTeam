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

from .models import FormaDePago
from .models import Iva
from .models import Tarjeta
from .models import Factura

from .serializers import FormaDePagoSerializer
from .serializers import IvaSerializer
from .serializers import TarjetaSerializer
from .serializers import FacturaSerializer
# Create your views here.

class FormaDePagoViewSet(viewsets.ModelViewSet):
    queryset = FormaDePago.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FormaDePagoSerializer

class IvaViewSet(viewsets.ModelViewSet):
    queryset = Iva.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = IvaSerializer


class TarjetaViewSet(viewsets.ModelViewSet):
    queryset = Tarjeta.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TarjetaSerializer


class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FacturaSerializer


@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def formaPagoAll(request):
    data = FormaDePago.objects.all()
    serializer = FormaDePagoSerializer(data, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([AllowAny])
def formaPago(request, pk):

    if(request.method=='GET'):
        data = generics.get_object_or_404(FormaDePago,id=pk)
        if data is not None:
            serializer = FormaDePagoSerializer(data, many=False)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'message': 'Forma de Pago no existe'},status=status.HTTP_400_BAD_REQUEST)

    elif(request.method=='POST' and request.user.is_authenticated):
        serializer = FormaDePagoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    elif(request.method=='PUT' and request.user.is_authenticated):
        data = generics.get_object_or_404(FormaDePago,id=pk)
        if data is not None:
            serializer = FormaDePagoSerializer(data, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Forma de Pago no existe'},status=status.HTTP_400_BAD_REQUEST)

    elif(request.method=='DELETE' and request.user.is_authenticated):
        data = generics.get_object_or_404(FormaDePago,id=pk)
        if data is not None:
            data.delete()
            msg={
                'message':'Forma de Pago eliminado exitosamente'
            }
            return Response(msg,status=status.HTTP_200_OK)
        return Response({'message': 'Forma de Pago no existe'},status=status.HTTP_400_BAD_REQUEST)

    else:
        msg={
            'error':'Permission Denied!'
        }
        return Response(msg,status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def ivaAll(request):
    data = Iva.objects.all()
    serializer = IvaSerializer(data, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([AllowAny])
def iva(request, pk):

    if(request.method=='GET'):
        data = generics.get_object_or_404(Iva,id=pk)
        if data is not None:
            serializer = IvaSerializer(data, many=False)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'message': 'Iva no existe'},status=status.HTTP_400_BAD_REQUEST)

    elif(request.method=='POST' and request.user.is_authenticated):
        serializer = IvaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    elif(request.method=='PUT' and request.user.is_authenticated):
        data = generics.get_object_or_404(Iva,id=pk)
        if data is not None:
            serializer = IvaSerializer(data, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Iva no existe'},status=status.HTTP_400_BAD_REQUEST)

    elif(request.method=='DELETE' and request.user.is_authenticated):
        data = generics.get_object_or_404(Iva,id=pk)
        if data is not None:
            data.delete()
            msg={
                'message':'Iva eliminado exitosamente'
            }
            return Response(msg,status=status.HTTP_200_OK)
        return Response({'message': 'Iva no existe'},status=status.HTTP_400_BAD_REQUEST)

    else:
        msg={
            'error':'Permission Denied!'
        }
        return Response(msg,status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def tarjetaAll(request):
    data = Tarjeta.objects.all()
    serializer = TarjetaSerializer(data, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([AllowAny])
def tarjeta(request, pk):

    if(request.method=='GET'):
        data = generics.get_object_or_404(Tarjeta,id=pk)
        if data is not None:
            serializer = TarjetaSerializer(data, many=False)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'message': 'Tarjeta no existe'},status=status.HTTP_400_BAD_REQUEST)

    elif(request.method=='POST' and request.user.is_authenticated):
        serializer = TarjetaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    elif(request.method=='PUT' and request.user.is_authenticated):
        data = generics.get_object_or_404(Tarjeta,id=pk)
        if data is not None:
            serializer = TarjetaSerializer(data, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Tarjeta no existe'},status=status.HTTP_400_BAD_REQUEST)

    elif(request.method=='DELETE' and request.user.is_authenticated):
        data = generics.get_object_or_404(Tarjeta,id=pk)
        if data is not None:
            data.delete()
            msg={
                'message':'Tarjeta eliminado exitosamente'
            }
            return Response(msg,status=status.HTTP_200_OK)
        return Response({'message': 'Tarjeta no existe'},status=status.HTTP_400_BAD_REQUEST)

    else:
        msg={
            'error':'Permission Denied!'
        }
        return Response(msg,status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def facturaAll(request):
    data = Factura.objects.all()
    serializer = FacturaSerializer(data, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([AllowAny])
def factura(request, pk):

    if(request.method=='GET'):
        data = generics.get_object_or_404(Factura,id=pk)
        if data is not None:
            serializer = FacturaSerializer(data, many=False)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'message': 'Factura no existe'},status=status.HTTP_400_BAD_REQUEST)

    elif(request.method=='POST' and request.user.is_authenticated):
        serializer = FacturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    elif(request.method=='PUT' and request.user.is_authenticated):
        data = generics.get_object_or_404(Factura,id=pk)
        if data is not None:
            serializer = FacturaSerializer(data, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Factura no existe'},status=status.HTTP_400_BAD_REQUEST)

    elif(request.method=='DELETE' and request.user.is_authenticated):
        data = generics.get_object_or_404(Factura,id=pk)
        if data is not None:
            data.delete()
            msg={
                'message':'Factura eliminado exitosamente'
            }
            return Response(msg,status=status.HTTP_200_OK)
        return Response({'message': 'Factura no existe'},status=status.HTTP_400_BAD_REQUEST)

    else:
        msg={
            'error':'Permission Denied!'
        }
        return Response(msg,status=status.HTTP_403_FORBIDDEN)