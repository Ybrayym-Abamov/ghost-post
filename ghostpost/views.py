from django.shortcuts import render, reverse, HttpResponseRedirect
from ghostpost.models import BoastsRoasts
from ghostpost.form import GhostPost

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
            BoastsRoasts.objects.create(
                boolean=data['boolean'],
                body=data['body']
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = GhostPost()
    return render(request, 'ghost.html', {'form': form})


# extra credit
def delete_post(request, id):
    post = BoastsRoasts.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect(reverse('homepage'))
