from django.contrib import admin

# Register your models here.
from .models import Animale
from .models import Colaboradore
from .models import Protectora

admin.site.register(Animale)
admin.site.register(Colaboradore)
admin.site.register(Protectora)