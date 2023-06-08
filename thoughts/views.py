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

        return redirect('/')

    return redirect('/404')