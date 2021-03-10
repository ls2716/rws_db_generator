from django.contrib import admin
from .models import BaseMeaning, Word
# Register your models here.
admin.site.register(Word)
admin.site.register(BaseMeaning)