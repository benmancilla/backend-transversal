from rest_framework import serializers
from . models import React,Contact

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['id', 'title', 'image', 'price']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'created_at']


