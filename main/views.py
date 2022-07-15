from django.shortcuts import render
from django.urls import reverse
from faker import Faker
from .models import *
import random


def generate_data(request):
    fake = Faker()
    for i in range(100):
        Object.objects.create(
            name=fake.name(),
            quantity=random.randint(0, 100)
        )
    return reverse('index')
