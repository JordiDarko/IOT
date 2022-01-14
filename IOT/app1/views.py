from django.shortcuts import render
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

def rele_on(request):
    if request.method == 'GET':
        GPIO.output(21, GPIO.HIGH)

def rele_off(request):
    if request.method == 'GET':
        GPIO.output(21, GPIO.LOW)
