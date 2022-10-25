from django.shortcuts import render
from rest_framework.generics import ListAPIView , RetrieveAPIView , ListCreateAPIView , RetrieveUpdateDestroyAPIView
from blog.models import Post , Rating
from .serializers import ListApiSerializers , DetailApiSerializers ,RatingApiSerializers
from rest_framework.permissions import IsAuthenticated
from .permissions import User_Permissions
# Create your views here.

class ListView(ListCreateAPIView):
    queryset =Post.objects.all()
    serializer_class = ListApiSerializers

class DetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = DetailApiSerializers
    permission_classes = (User_Permissions,)
    
class RatingView(ListCreateAPIView):
    queryset =Rating.objects.all()
    serializer_class = RatingApiSerializers