from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

@api_view(('GET',))
def rele_on(request):
    if request.method == 'GET':
        GPIO.output(21, GPIO.HIGH)
        content = {'RELE': 'ON'}
        return Response(content, status=status.HTTP_200_OK)

def rele_off(request):
    if request.method == 'GET':
        GPIO.output(21, GPIO.LOW)
        content = {'RELE': 'OFF'}
        return Response(content, status=status.HTTP_200_OK)