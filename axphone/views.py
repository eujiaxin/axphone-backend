from django.shortcuts import render
from .serializers import ContactSerializer
from rest_framework import viewsets
from .models import Contact

# Create your views here.


class ContactView(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
