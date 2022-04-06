from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog
from .forms import BlogForm, EditForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Blog
    template_name = 'home.html'
    ordering = ['-id']


class RecipeDescription(DetailView):
    model = Blog
    template_name = 'recipe_details.html'


class NewDishCard(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'add_blog.html'


class EditBlogView(UpdateView):
    model = Blog
    template_name = 'edit_blog.html'
    form_class = EditForm


class DeleteBlogView(DeleteView):
    model = Blog
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('home')
