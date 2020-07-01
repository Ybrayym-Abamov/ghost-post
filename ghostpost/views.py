from django.shortcuts import render, reverse, HttpResponseRedirect
from ghostpost.models import BoastsRoasts
from ghostpost.form import GhostPost

from string import ascii_lowercase
from random import choice

# Create your views here.


def main(request):
    data = BoastsRoasts.objects.order_by("-datetime")
    return render(request, "main.html", {'data': data})


def boasts(request):
    data = BoastsRoasts.objects.filter(boolean=True).order_by("-datetime")
    return render(request, "main.html", {"data": data})


def roasts(request):
    data = BoastsRoasts.objects.filter(boolean=False).order_by("-datetime")
    return render(request, "main.html", {"data": data})


def upvote(request, postid):
    post = BoastsRoasts.objects.get(id=postid)
    post.upvotes += 1
    post.save()
    return HttpResponseRedirect(reverse('sortscore', kwargs={'post': postid}))


def downvote(request, postid):
    post = BoastsRoasts.objects.get(id=postid)
    post.downvotes += 1
    post.save()
    return HttpResponseRedirect(reverse('sortscore', kwargs={'post': postid}))


def sortscore(request, post):
    post = BoastsRoasts.objects.get(id=post)
    post.score = post.upvotes - post.downvotes
    post.save()
    return HttpResponseRedirect(reverse('homepage'))


def mostpopular(request):
    data = BoastsRoasts.objects.all().order_by('-score')
    return render(request, 'main.html', {'data': data})


def ghostsubmission(request):
    if request.method == "POST":
        form = GhostPost(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            key = ''.join(choice(ascii_lowercase) for i in range(10))
            BoastsRoasts.objects.create(
                boolean=data['boolean'],
                body=data['body'],
                secret_id=key
            )
            return render(request, 'delete.html', {'key': key})
    form = GhostPost()
    return render(request, 'ghost.html', {'form': form})


# extra credit
def private_view(request, private_key):
    data = BoastsRoasts.objects.get(secret_id=private_key)
    return render(request, 'main.html', {'data': data})


def delete_post(request, pk):
    post = BoastsRoasts.objects.get(secret_id=pk)
    post.delete()
    return HttpResponseRedirect(reverse('homepage'))
