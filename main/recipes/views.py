from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Category, Ingredient
from .serializers import CategorySerializer, IngredientSerializer


class CategoryApiView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def list(self, request):
        categories = Category.objects.all()
        data = [x.to_json() for x in categories]
        return Response(data)
        
    

class IngredientApiView(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer 
    
    
    def list(self, request):
        ingredients = Ingredient.objects.all()
        data = [x.to_json() for x in ingredients]
        return Response(data)