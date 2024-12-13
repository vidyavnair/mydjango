from django.shortcuts import render
from .models import Full_data
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .serializers import Full_data_serializers
# Create your views here.

# @api_view(['GET'])
# def index_display(request):
#     people={'name':'keerthi',
#             'age':24,
#             'place':'pandalam'}
#     return Response(people)

@api_view(['GET','POST','PATCH','PUT','DELETE'])
def person(request):
        if request.method=='GET':
                myobj=Full_data.objects.all()
                serializer=Full_data_serializers(myobj,many=True)
                return Response(serializer.data)
        elif request.method=='POST':
                data=request.data
                serializer=Full_data_serializers(data=data)
                if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                return Response(serializer.errors)
        elif request.method=='PUT':
                
                data=request.data
                obj=Full_data.objects.get(id=data['id'])
                serializer=Full_data_serializers(obj,data=data,partial=False)
                if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                return Response(serializer.errors)
        elif request.method=='PATCH':
                
                data=request.data
                obj=Full_data.objects.get(id=data['id'])
                serializer=Full_data_serializers(obj,data=data,partial=True)
                if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                return Response(serializer.errors)
@api_view(['GET'])      

def single_details(request,pk):
        datas=Full_data.objects.get(id=pk)
        serializer=Full_data_serializers(datas,many=False)
        return Response(serializer.data)