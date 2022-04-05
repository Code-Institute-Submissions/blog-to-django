from django.urls import path
from .views import HomeView, RecipeDescription, NewDishCard

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('recipe/<int:pk>', RecipeDescription.as_view(), name='recipe'),
    path('add_blog/', NewDishCard.as_view(), name='new_blog'),
]
