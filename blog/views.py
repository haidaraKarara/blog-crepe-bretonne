from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse

from .models import Article, Comment
from .forms import CommentForm


def accueil(request):
    """
    Affiche les 5 derniers articles du blog. Nous n'avons pas encore
    vu comment faire de la pagination, donc on ne donne pas la
    possibilité de lire les articles plus vieux via l'accueil pour
    le moment.
    """
    articles = Article.objects.filter(is_visible=True).order_by('-date')[:5]
    """ recupération du nombre de commentaire(s) pour les 5 derniers articles """
    return render(request, 'blog/accueil.html',locals())

def lire_article(request, slug):
    """
    Affiche un article complet, sélectionné en fonction du slug
    fourni en paramètre
    """
    article = get_object_or_404(Article, slug=slug)
    """ Recupération de tous les commentaires d'un article """
    commentaires = Comment.objects.filter(article=article).order_by('-date')
    form = CommentForm()
    return render(request, 'blog/lire_article.html',locals())

def creer_comment(request,id):
    """ récupération de l'article concerné """
    article_recup = get_object_or_404(Article, id=id)
    article_recup.nbr_comment += 1
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment()
            comment.pseudo = form.cleaned_data['pseudo']
            comment.email = form.cleaned_data['email']
            comment.contenu = form.cleaned_data['contenu']
            comment.article = article_recup
            comment.save()
            article_recup.save()
    chaine = article_recup.slug
    return redirect('blog_lire',slug=chaine)