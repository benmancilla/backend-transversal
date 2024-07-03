from rest_framework import generics, status, permissions
from rest_framework import generics, status
from rest_framework.response import Response
from .models import React,Contact
from .serializer import ReactSerializer,ContactSerializer
from .permissions import IsAuthenticatedOrReadOnly

class ReactView(generics.ListCreateAPIView):
    queryset = React.objects.all()
    serializer_class = ReactSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ContactView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







