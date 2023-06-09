from django.contrib.auth.decorators import login_required
from django.db.models import Case, Value, When, CharField
from django.db.models.functions import Concat
from django.shortcuts import redirect, render
from django.urls import reverse
import random

from constants.anonymous_profiles import RESERVED_ANON_NAME, ANON_NAMES
from thoughts.models import Thought, Comment, Anonymous_Profile

# Create your views here.
# function to generate Anonymous Names
def generate_anon_name(thought_id):
    # fetch all the used anonymous name for the specific post
    used_anon_names = Anonymous_Profile.objects.filter(linked_post = thought_id).values('anonymous_name')
    used_anon_names = set(used_anon_name['anonymous_name'] for used_anon_name in used_anon_names)

    # ignore used anonymous name from all the available anonymous names
    available_anon_names = ANON_NAMES - used_anon_names
    # randomly choose anonymous name from available list
    anon_name = random.choice(list(available_anon_names))

    return anon_name


@login_required
def create_post(request):
    if request.method == "POST":
        content = request.POST['thought']
        anonymous = True if request.POST.get('anonymous') else False
        current_user = request.user

        thought = Thought.objects.create(content = content, author = current_user, anonymous = anonymous)

        if anonymous:
            # reserved anon name given to only Post Owners
            anon_name = RESERVED_ANON_NAME
            anon_profile = Anonymous_Profile.objects.create(
                author = current_user, 
                linked_post = thought, 
                anonymous_name = anon_name
                )
    
        return redirect('/')

    return redirect('/404')

@login_required
def show_post(request, id):
    try:
        current_user  = request.user
        # fetch the thought with the specific id
        thought = Thought.objects.filter(id = id).annotate(
        username = Case(
            When(anonymous=True, then=Concat(Value('Anonymous '), 'anonymous_profile__anonymous_name')),
            When(anonymous=False, then='author__username'),
            output_field=CharField(),
        ),).values('id', 'username', 'content', 'date_time')

        # fetch all the anonymous profile associated with the post
        anon_profile_associated = Anonymous_Profile.objects.filter(linked_post = id).values('author__username', 'anonymous_name')
        anon_profiles = {}
        # link author names with the anonymous name alloted
        for data in anon_profile_associated:
            anon_profiles[data['author__username']] = data['anonymous_name']

        # fetch all the comments for the specific post
        # with all the confidential information
        raw_comments = Comment.objects.filter(linked_post = id).annotate(
            can_delete=Case(
            When(author=current_user, then=Value('True')),
            default=Value('False'),
            output_field=CharField()
            ),).values('id', 'content', 'date_time', 'author__username', 'anonymous','can_delete')
        
        comments = []
        for comment in raw_comments:
            # if user choose to be anonymous
            # use the anon name that has been allocated to them
            if comment['anonymous']:
                username = 'Anonymous ' + anon_profiles[comment['author__username']]
            else:
                username = comment['author__username']
            
            comments.append({'id': comment['id'], 
                             'content': comment['content'], 
                             'date_time': comment['date_time'], 
                             'username': username, 
                             'can_delete': comment['can_delete']})

        return render(request, 'thoughts/index.html', {'thought': thought[0], 'comments': comments})
    except:
        return redirect('/404')

def write_comment(request, id):
    content = request.POST['thought']
    anonymous = True if request.POST.get('anonymous') else False
    current_user = request.user
    linked_post = Thought.objects.get(id = id)

    comment = Comment.objects.create(content = content, author = current_user, linked_post = linked_post, anonymous = anonymous)

    if anonymous:
        anon_profile, created = Anonymous_Profile.objects.get_or_create(author = current_user, linked_post = linked_post)

        # if new entry is created, generate a random anon name for the user
        if created:
            anon_name = generate_anon_name(id)
            anon_profile.anonymous_name = anon_name
            anon_profile.save()

    redirect_url = reverse(show_post, kwargs={'id': id})
    
    # Redirect to the dynamic URL
    return redirect(redirect_url)
    
@login_required
def delete_post(request, id):
    try:
        current_user = request.user
        thought = Thought.objects.get(id = id, author = current_user)
        
        # check whether the author is deleting the post or not
        if thought:
            thought.status = '2'
            thought.save()

            return redirect('/')
        else:
            return redirect('/404')
    except:
        return redirect('/404')