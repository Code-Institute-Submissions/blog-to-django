from django.urls import path
from .views import HomeView, RecipeDescription, NewDishCard, EditBlogView, DeleteBlogView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('recipe/<int:pk>', RecipeDescription.as_view(), name='recipe'),
    path('add_blog/', NewDishCard.as_view(), name='new_blog'),
    path('recipe/edit_blog/<int:pk>', EditBlogView.as_view(
        ), name='edit_blog'),
    path('recipe/<int:pk>/delete_blog', DeleteBlogView.as_view(
    ), name='delete_blog'),
]
