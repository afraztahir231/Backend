from django.shortcuts import render
from django.http import FileResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import userSerializer
from .models import User
import base64
import cv2 as cv
import numpy as np
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint' : '/credentials/',
            'method' : 'POST',
            'body' : None,
            'description' : 'takes the user entered credentials.'
        },
        {
            'Endpoint' : '/confirm/',
            'method' : 'GET',
            'body' : None,
            'description' : 'this will confirm the credentials.'
        },
        {
            'Endpoint' : '/enhance/',
            'method' : 'GET',
            'body' : None,
            'description' : 'this will send the enhanced photo.'
        },
        {
            'Endpoint' : '/upload/',
            'method' : 'POST',
            'body' : None,
            'description' : 'this will take the image from user.',
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getInfo(request):
    user = User.objects.all()
    serializer = userSerializer(user, many = True)

    return Response(serializer.data)

@api_view(['GET'])
def getImage(request, username):
    instance = get_object_or_404(User, name=username)
    image_path = instance.enhanced.path  # Assuming 'image' is the ImageField in your model

    # Serve the image using FileResponse
    return FileResponse(open(image_path, 'rb'), content_type='image/jpeg')

@api_view(['POST'])
def upload_image(request):
    obj = User.objects.get(name = "Afraz Tahir")
    image = request.FILES.get('image')

    image_data = image.read()
    image_ = cv.imdecode(np.frombuffer(image_data, np.uint8), cv.IMREAD_COLOR)

    cv.imshow("Uploaded Image", image_)
    cv.waitKey(0);

    if image:
        #obj.images += image
        #obj.save()
        return Response({'message': 'Image uploaded successfully'}, status=201)
    return Response({'error': 'No image provided'}, status=400)
