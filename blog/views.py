from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect

from blog.models import Post, PostCategory, Comment
from blog import model_helpers
from blog import navigation
from blog.forms import CommentForm

def post_list(request, category_name=model_helpers.post_category_all.slug()):
    category, posts = model_helpers.get_category_and_posts(category_name)
    categories = model_helpers.get_categories()

    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_POSTS),
        'category': category,
        'posts': posts,
        'categories': categories,
    }

    return render(request, 'blog/post_list.html', context)


def post_detail(request, post_id, message=''):

    post = get_object_or_404(Post, pk=post_id)

    # Les posts de la meme categorie sauf l'element actuel
    posts_same_category = Post.objects.filter(published=True, category=post.category).exclude(pk=post_id)

    # Les commentaires associés au post
    #comments = Comment.objects.filter(post=post.pk)
    #comments = post.comment_set.all()
    comments = post.comments.exclude(status=Comment.STATUS_HIDDEN)

    # Enregristrement d'un nouveau commentaire
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        # Si le commentaire est valide. Récupérer la FK du post associé.
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            # Traitement du message
            args = [post.pk, 'Your comment has been posted!']
            return HttpResponseRedirect(reverse('post-detail-message', args=args) + '#comments')


    else:
        comment_form = CommentForm()

    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_POSTS),
        'post': post,
        'posts_same_category': posts_same_category,
        'comments': comments,
        'comment_form': comment_form,
        'message': message,
    }

    return render(request, 'blog/post_detail.html', context)


def about(request):
    context = {
        'navigation_items': navigation.navigation_items(navigation.NAV_ABOUT),
    }

    return render(request, 'blog/about.html', context)