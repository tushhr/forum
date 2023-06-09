from django.shortcuts import redirect

from .models import Thought

# Create your views here.
def create_post(request):
    if request.method == "POST":
        content = request.POST['thought']
        anonymous = request.POST.get('anonymous')
        current_user = request.user

        thought = Thought(content = content, author = current_user)
        if anonymous:
            thought.anonymous = True
        
        thought.save()

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