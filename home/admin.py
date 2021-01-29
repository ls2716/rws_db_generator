from django.contrib import admin
from .models import BaseMeaning, Person, Word
# Register your models here.
admin.site.register(Person)
admin.site.register(Word)
admin.site.register(BaseMeaning)