from django.db import models
from django.utils import timezone

class Comment(models.Model):
    """ Modèle pour les commentaires. A vous de l'écrire ! """
    pseudo = models.CharField(max_length=25)
    email = models.EmailField("Votre Email",null=True)
    contenu = models.TextField()
    date = models.DateTimeField(verbose_name="Date de commentaire",default=timezone.now)
    article = models.ForeignKey('Article',on_delete=models.CASCADE)

    def __str__(self):
        return self.pseudo

    class Meta:
        verbose_name = "< Commentaire >"
        verbose_name_plural = "< Commentaires >"
    

class Article(models.Model):
    titre = models.CharField(max_length=100)
    slug = models.SlugField()
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(verbose_name="Date de parution",
                                auto_now_add=True, auto_now=False)
    is_visible = models.BooleanField(verbose_name="Article publié ?",
                                     default=False)
    categorie = models.ForeignKey('Categorie',on_delete=models.CASCADE)
    nbr_comment = models.IntegerField(default=0)

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = "< Article >"
        verbose_name_plural = "< Articles >"


class Categorie(models.Model):
    titre = models.CharField(max_length=100)

    def __str__(self):
        return self.titre
    class Meta:
        verbose_name = "< Categorie >"
        verbose_name_plural = "< Categories >"