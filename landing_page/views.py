from django.db.models import Case, Value, When, CharField
from django.shortcuts import render
from django.db.models.functions import Concat

from constants.anonymous_profiles import RESERVED_ANON_NAME
from thoughts.models import Thought

def index(request):
    current_user = request.user
    all_thoughts = {}

    if current_user.is_authenticated:
        all_thoughts = Thought.objects.exclude(status__in = ['2', '3']).annotate(
        username=Case(
            When(anonymous=True, then=Concat(Value('Anonymous '), Value(RESERVED_ANON_NAME))),
            When(anonymous=False, then='author__username'),
            output_field=CharField()
        )).annotate(
            can_delete=Case(
                When(author=current_user, then=Value('True')),
                default=Value('False'),
                output_field=CharField()
            )
        ).values('id', 'username', 'content', 'date_time', 'can_delete').order_by('-date_time')


    return render(request, 'landing_page/index.html', {'thoughts': all_thoughts})

def error(request):
    return render(request, 'landing_page/error.html')