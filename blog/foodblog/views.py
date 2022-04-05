from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Blog


class HomeView(ListView):

    model = Blog
    template_name = 'home.html'


class RecipeDescription(DetailView):
    model = Blog
    template_name = 'recipe_details.html'


class NewDishCard(CreateView):
    model = Blog
    template_name = 'add_blog.html'
    fields = '__all__'

