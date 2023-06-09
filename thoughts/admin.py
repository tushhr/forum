from django.contrib import admin
from .models import Thought, Comment, Anonymous_Profile

admin.site.register(Thought)
admin.site.register(Comment)
admin.site.register(Anonymous_Profile)
