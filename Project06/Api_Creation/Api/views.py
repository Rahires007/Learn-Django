from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializer import StudentSerializer
from .models import Students


# Create your views here.
@api_view(["GET", "POST", "DELETE", "PUT", "PATCH"])   #HTTP method work on api 
def Api_Create_View(request):

    # GET Method
    if request.method == "GET":
        students = Students.objects.all()   #Get all records from models & store
        serializer = StudentSerializer(students, many=True)  #Serialize & store data

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )   #Give Responce

    # POST Method
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)   #Serialize & store data extract from request

        if serializer.is_valid():  #Serialize data is valid 
            serializer.save()   #save the data

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )  #Give Responce

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )    #Give Error Responce

    # DELETE Method
    elif request.method == "DELETE":
        Id = request.data.get("id")   #Extract id from request 

        student = Students.objects.filter(id=Id).first()  #Find Record using id & filter & first

        if student is not None:   #Check it none
            student.delete()   #Delete record

            return Response(
                status=status.HTTP_204_NO_CONTENT
            )   # Give Responce

        else:
            return Response(
                {"error": "Student not found"},
                status=status.HTTP_404_NOT_FOUND
            )  #Give Error Responce

    # PUT Method
    elif request.method == "PUT":
        Id = request.data.get("id") #Extract id from request

        student = Students.objects.filter(id=Id).first()  #Find Record using id

        if student is not None:  #Check it none
            serializer = StudentSerializer(
                student,
                data=request.data
            )   #Serialize data

            if serializer.is_valid():  #Check Serializer data is valid
                serializer.save()   #Save the data

                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )  #Give Responce

            else:
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )  #Give Error Responce

        else:
            return Response(
                {"error": "Student not found"},
                status=status.HTTP_404_NOT_FOUND
            ) #Give Error Responce 

    # PATCH Method
    elif request.method == "PATCH":
        Id = request.data.get("id")   #Extract Id

        student = Students.objects.filter(id=Id).first()  #Find Record using id

        if student is not None:
            serializer = StudentSerializer(
                student,
                data=request.data,
                partial=True
            )   #Serialize & Store data

            if serializer.is_valid():
                serializer.save()  #Save data

                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )   #Give Responce

            else:
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )   #Give Error Responce

        else:
            return Response(
                {"error": "Student not found"},
                status=status.HTTP_404_NOT_FOUND
            )   #Give Error Responce
