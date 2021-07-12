import os

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView
from .models import Glasses, UserPhoto, Shape
from blog.forms import ImageForm

from blog import algorithm


class AnswerView(DetailView):
    template_name = 'blog/result.html'
    model = UserPhoto


class SortView(CreateView):
    template_name = 'blog/home.html'
    model = UserPhoto
    form_class = ImageForm

    def get_success_url(self):
        my_object = UserPhoto.objects.latest('pk')
        if my_object:
            absolute_path = os.path.join(os.getcwd(), 'media', 'images', os.path.split(my_object.image.url)[1])
            face_landmarks = algorithm.get_face_landmarks(absolute_path)
            if algorithm.is_triangle(face_landmarks):
                my_object.shape = Shape.objects.get(shape='triangle')
            else:
                if algorithm.is_face_long(face_landmarks):
                    if algorithm.is_square(face_landmarks):
                        my_object.shape = Shape.objects.get(shape='rectangle')
                    else:
                        my_object.shape = Shape.objects.get(shape='oval')
                else:
                    if algorithm.is_square(face_landmarks):
                        my_object.shape = Shape.objects.get(shape='square')
                    else:
                        my_object.shape = Shape.objects.get(shape='circle')
            my_object.glasses.set(Glasses.objects.filter(shape=my_object.shape))
            print(type(my_object.glasses))
        my_object.save()
        return f"result/{my_object.pk}"

