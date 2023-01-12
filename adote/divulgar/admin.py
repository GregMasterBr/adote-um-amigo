from django.contrib import admin
from .models import Raca, Tag, Pet

# Register your models here.

from .models import *

admin.site.register(Raca)
admin.site.register(Tag)
admin.site.register(Pet)