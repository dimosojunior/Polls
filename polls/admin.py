from django.contrib import admin
from .models import *

admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Vote)
admin.site.register(ElectionCategories)
