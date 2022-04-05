from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Blog
from .forms import BlogForm


class HomeView(ListView):

    model = Blog
    template_name = 'home.html'


class RecipeDescription(DetailView):
    model = Blog
    template_name = 'recipe_details.html'


class NewDishCard(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'add_blog.html'