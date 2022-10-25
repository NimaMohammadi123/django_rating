from django.core import paginator
from django.shortcuts import render , get_object_or_404
from .models import Post, Rating
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from django.views.generic import ListView
from .form import EmailPostForm ,Post_Form ,Rating_Form

# Create your views here.

    
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 2
    template_name = 'blog/post/list.html'
    

def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post , slug = post ,status = "published", publish__year = year, publish__month = month , publish__day = day)
    #form =Post_Form()
    #if request.method=='POST':
     #   form = Post_Form(request.POST)
      #  if form.is_valid:
       #     form.save(commit=False)
        #    post.rating=form.cleaned_data['rating']
         #   post.rating_user.add(request.user)
          #  if post.rating_user.filter(id=request.user.id):
           #     post.rating_user.update(request.user)
            #    form.save()
            #form.save()
            
    form = Rating_Form()
    try:
        rating=Rating.objects.get(user__id=request.user.id,post__id=post.id)
        form = Rating_Form(request.POST,instance=rating)
        return render(request , 'blog/post/detail.html',{"post": post,'form':form})
    
    except Rating.DoesNotExist:
        if request.method == 'POST':
            form = Post_Form(request.POST)
        if form.is_valid:
            rating = Rating()
            rating.post = post
            rating.user=request.user
            rating.rating = form.cleaned_data['rating']
            rating.save()
    return render(request , 'blog/post/detail.html',{"post": post,'form':form})


def post_share(request,post_id):
    post = get_object_or_404(Post,id=post_id,status="published")
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url())
            subject = f"{cd['name']} recommend you"
            message = f"{post.title} in {post_url} and {cd['comment']}"
            send_mail(
                subject,message,"admin@gmail.com",
                [cd['to']]
            )

    else:
        form = EmailPostForm()
    return render(request,'blog/post/share.html',{'post':post,'form':form})