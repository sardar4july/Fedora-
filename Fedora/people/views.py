from django.shortcuts import render
from.models import Person
from .serializers import PersonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view
def list_people(request):
    people=Person.objects.all()
    serializer=PersonSerializer(people,many=True)
    content={
        "people":serializer.data
    }
    return Response(content)