from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from mgmtapp.serializers import *
from django.views.decorators.csrf import csrf_exempt
from mgmtapp.models import *
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User,UserManager
from rest_framework.authtoken import views as tokenView
from django.db.models import *
import string
import datetime
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework import generics

class Disc_type_list(APIView):
    

    #1. Get all discussions which type is Either Article or Question
   
    def get(self, request, format=None):
        result_list =[]
        # list1 = Discussion.objects.all().filter(discussion_type='question')
        # list2 = Discussion.objects.all().filter(discussion_type='article')
        # for x in list1:
        #     result_list.append(x)
        # for x in list2:
        #     result_list.append(x)
        result_list = Discussion.objects.filter(discussion_type__in=['question','article'])
        discussions = result_list
        serializer = DiscussionListSerializer(discussions, many=True)
        print serializer.data
        return Response(serializer.data, status=status.HTTP_200_OK)

class Get_search_Disc_title(APIView):

    #3. Get all discussions which title matches searched term example: /api/discussion/list/?title=Sports
    
    def get(self, request, format=None):
        lis=['title']
        lis2 = list(request.GET)
        print lis
        print lis2
        if lis == lis2 :
            title = request.GET['title']  
            print title
            discussion = Discussion.objects.filter(title__icontains=title)
            print discussion
            serializer = DiscussionListSerializer(discussion, many=True)    
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'please enter title in URL'}, status=status.HTTP_200_OK)



class Disc_search_by_title_text_disctype(APIView):
    #4. Discussion should be searched by title, text and discussion_type    
    def get(self, request, format=None):
        lis=['discussion_type','text','title']
        lis2=list(request.GET)
        print lis
        print lis2[0]
        if lis == lis2:    
            title = request.GET['title']
            text = request.GET['text']
            discussion_type = request.GET['discussion_type']
            print title
            discussion = Discussion.objects.filter(Q(title__icontains=title) | Q(discussion_type__icontains=discussion_type) | Q(text__icontains=text))   
            print discussion
            serializer = DiscussionListSerializer(discussion, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'please enter title,text,discussion_type in URL in this sequence   '}, status=status.HTTP_200_OK)



#@authentication_classes((TokenAuthentication,))
class Create_comment(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    #2.Add comment api notes:only logged in user can add comment one user can not add more than 1 
    def post(self, request, format=None):
        if request.user.is_authenticated():
            data=request.data
            data['added_by']=request.user.id
            disid=request.data['discussion']
            comment = Comment.objects.all().filter(discussion=disid, added_by=request.user).exists()
            if comment == True:
                return Response({'error': 'You already commented earlier.'}, status=status.HTTP_200_OK)
            else:
                #res= Discussion.objects.get(id =disid)
                result=Discussion.objects.filter(creater_id__added_by = request.user).exists()
                if result:
                    return Response({'error': 'You can not comment on your Discussion'}, status=status.HTTP_200_OK)
                else:
                    serializer = CommentSerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)











# #1. Get all discussions which type is Either Article or Question
@csrf_exempt
@api_view(['GET'])
def discussions_list(request):
    result_list =[]
    # list1 = Discussion.objects.all().filter(discussion_type='question')
    # list2 = Discussion.objects.all().filter(discussion_type='article')
    # for x in list1:
    #     result_list.append(x)
    # for x in list2:
    #     result_list.append(x)
    result_list = Discussion.objects.filter(discussion_type__in=['question','article'])
    discussions = result_list
    serializer = DiscussionListSerializer(discussions, many=True)
    print serializer.data
    return Response(serializer.data, status=status.HTTP_200_OK)







# #2. Add comment api notes:only logged in user can add comment one user can not add more than 1 
# #   comment in particular discussion user can not comment on his own created discussion
@csrf_exempt
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
def comment_create(request):
    if request.user.is_authenticated():
        data=request.data
        data['added_by']=request.user.id
        disid=request.data['discussion']
        comment = Comment.objects.all().filter(discussion=disid, added_by=request.user).exists()
        if comment == True:
            return Response({'error': 'You already commented earlier.'}, status=status.HTTP_200_OK)
        else:
            res= Discussion.objects.get(id =disid)
            result=Discussion.objects.filter(added_by = request.user)
            if res in result:
                return Response({'error': 'You can not comment on your Discussion'}, status=status.HTTP_200_OK)
            else:
                serializer = CommentSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)



# #3. Get all discussions which title matches searched term example: /api/discussion/list/?title=Sports
@csrf_exempt
@api_view(['GET'])
def DiscussionListSearch(request):
    lis=['title']
    lis2 = list(request.GET)
    if lis == lis2 :
        title = request.GET['title']            
        print title
        discussion = Discussion.objects.filter(title__icontains=title)
        print discussion
        serializer = DiscussionListSerializer(discussion, many=True)    
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'please enter title in URL'}, status=status.HTTP_200_OK)







#4. Discussion should be searched by title, text and discussion_type
@csrf_exempt
@api_view(['GET'])
def DiscussionListSearchAll(request):
    lis=['discussion_type','text','title']
    lis2=list(request.GET)
    print lis
    print lis2
    if lis == lis2:    
        title = request.GET['title']
        text = request.GET['text']
        discussion_type = request.GET['discussion_type']
        print title
        discussion = Discussion.objects.filter(Q(title__icontains=title) | Q(discussion_type__icontains=discussion_type) | Q(text__icontains=text))   
        print discussion
        serializer = DiscussionListSerializer(discussion, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'please enter title,text,discussion_type in URL in this sequence   '}, status=status.HTTP_200_OK)



