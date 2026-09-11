from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializer import StudentSerializer
from .models import Students
# Create your views here.
@api_view(["GET","POST","DELETE","PUT"])
def Api_Create_View(request):
    if request.method=="GET":   #Get Method
        students=Students.objects.all() #Get all students from models & store in students
        serializer=StudentSerializer(students,many=True)  #Serialize all students mean convert The queryset into json
        return Response(serializer.data,status=status.HTTP_200_OK)  #Give Responce with Status code
    elif request.method=="POST":
        serializer=StudentSerializer(data=request.data)  #Extract data from request & serilize it 
        if serializer.is_valid(): #Check data inside serilizer is valid or not 
            serializer.save()   #Save data in the model
            return Response(serializer.data,status=status.HTTP_201_CREATED)  #Responce with status code
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        Id=request.data.get("id")   #Extract id from request
        student=Students.objects.get("id=Id")   #Find the student by using id
        if student is not None:  #Student if present 
            student.delete()   #
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="PUT":
        Id=request.data.get("id")
        student=Students.objects.get("id=Id")
        if student is not None:
            serializer=StudentSerializer(student,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)        