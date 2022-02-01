from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import IngredientApiView, CategoryApiView


router = DefaultRouter()
router.register('categories', CategoryApiView)
router.register('ingredients', IngredientApiView)

urlpatterns = [
    path('api/', include(router.urls))
]