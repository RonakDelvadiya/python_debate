from rest_framework.response import Response
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import datetime


class DiscussionListSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Discussion

class CommentSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Comment
        exclude = ('created_date', 'modified_date')
