from django.contrib import admin
from .models import Thought, Comment, anonymousProfile

admin.site.register(Thought)
admin.site.register(Comment)
admin.site.register(anonymousProfile)
