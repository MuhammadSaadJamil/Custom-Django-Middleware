from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView
from faker import Faker
from .models import *


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Main'
        data['header'] = 'Main Menu'
        return data


index = Index.as_view()


def generate_data(request):
    fake = Faker()
    for i in range(100):
        Person.objects.create(
            name=fake.name(),
            mobile=fake.phone_number()
        )
    return redirect(reverse('index'))


class PersonList(ListView):
    template_name = 'people_list.html'
    model = Person
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'People'
        data['header'] = 'People [ Class ]'
        return data


person_list = PersonList.as_view()


def people_list(request):
    people = Person.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(people, 10)

    try:
        people = paginator.page(page)
    except PageNotAnInteger:
        people = paginator.page(1)
    except EmptyPage:
        people = paginator.page(paginator.num_pages)

    data = {
        'object_list': people,
        'is_paginated': True,
        'users': people,
        'func': True,
        'title': 'People',
        'header': "People [ Func ]"

    }
    return render(request, 'people_list.html', data)
