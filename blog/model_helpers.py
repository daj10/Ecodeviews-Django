from blog.models import Post, PostCategory


post_category_all = PostCategory(name='All')

def get_category_and_posts(category_name):
    '''

    fonction pour recuper les posts et categories associées. Si n'existe pas renvoit object iterable null
    Plus pratique pour les BD
    :param category_name:
    '''
    posts = Post.objects.filter(published=True)

    if category_name == post_category_all.slug():
        category = post_category_all
    else:
        try:
            # Correspondance insensible à la casse
            category = PostCategory.objects.get(name__iexact=category_name)
            posts = posts.filter(category=category)
        except PostCategory.DoesNotExist:
            category = PostCategory(name=category_name)

            # Liste objet vide
            posts = Post.objects.none()

    # Filter post by date
    posts = posts.order_by('-created_at')

    return category, posts


def get_categories():

    # Prendre en compte la categorie all qu'on à créer
    #categories = PostCategory.objects.all()
    categories = list(PostCategory.objects.all())
    categories.insert(0, post_category_all)

    return categories
