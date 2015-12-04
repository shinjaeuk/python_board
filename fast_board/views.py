from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


from .models import Post
from .models import Comment
from .models import Category

# Create your views here.
def list_posts(request):
	per_page = 10
	page = request.GET.get('page', 1) 

	posts = Post.objects.all().order_by('-created_at')

	paginator = Paginator(posts, per_page)

	try:
		pg = paginator.page(page)
		print(pg)
	except PageNotAnInteger:
		pg = paginator.page(page)
		print(pg)
	except EmptyPage:
		pg = []

	return render(request, 'list.html', {
		'posts' : pg,
	})

def view_post(request, pk):

	post = get_object_or_404(Post, pk=pk)

	comments = post.comment_set.all()

	return render(request, 'view.html', {
		'post' : post,
		'comments' : comments,
	})

	
def create_post(request):

	if request.method == "GET":
		categories = Category.objects.all()

		print(categories)

		return render(request, 'edit.html',{
			'categories':categories,
		})
	elif request.method == "POST":

		cat = Category.objects.get(pk=request.POST['category'])

		post = Post(
				title = request.POST['title'],
				content = request.POST['content'],
				category = cat,
				)
		post.save()

		return redirect(post)
	else:
		pass

def edit_post(request, pk):

	if request.method == "GET":
		post = get_object_or_404(Post, pk=pk)
		categories = Category.objects.all()

		return render(request, 'edit.html', {
			'post':post,
			'categories':categories,
	})
	elif request.method == "POST":

		cat = Category.objects.get(pk=request.POST['category'])

		pk = request.POST['pk']

		post = Post.objects.get(pk=pk)
		post.title = title = request.POST['title']
		post.content = content = request.POST['content']
		post.category = cat
		post.save()

		return redirect(post);

	else:
		pass

def delet_comment(request, pk):

	post_id = request.POST['post_id']

	comment = Comment.objects.get(pk=pk)
	comment.delete()

	post = Post.objects.get(pk=post_id)
	post.save()
	
	return redirect(post);

def create_comment(request):

	comment_content = request.POST['comment_content']
	comment = Comment()
	comment.content = comment_content

	pk = request.POST['pk']
	post = Post.objects.get(pk=pk)

	post.comment_set.add(comment);
	post.save()

	return redirect(post)
