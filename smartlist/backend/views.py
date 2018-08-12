from .models import ShoppingList, Product, Entry
from .serializers import ShoppingListSerializer, ProductSerializer, EntrySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class ShoppingListsOfUser(APIView):

    def get(self, request, format=None):
        shoppingLists = ShoppingList.objects.all()
        #print(shoppingLists.get(id=1).entry_set)
        serializer = ShoppingListSerializer(shoppingLists, many=True)
        return Response(serializer.data)


class ShoppingLists(APIView):
    
    def getObject(self, pk):
        try:
            return ShoppingList.objects.get(id=pk)
        except ShoppingList.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        shoppingList = self.getObject(pk)
        serializer = ShoppingListSerializer(shoppingList)
        return Response(serializer.data)

class Entries(APIView):
    
    def post(self, request, format=None):
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()


#class EntriesDetail(APIView):

