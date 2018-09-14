from django.contrib import admin

from .models import Article, Categorie, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'categorie', 'date', 'is_visible','nbr_comment')
    list_filter = ('categorie', )
    search_fields = ('title', 'auteur', )
   # ordering       = ('-date', )
    prepopulated_fields = {'slug': ('titre', )}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pseudo', 'email', 'contenu', 'article','date' )
    list_filter = ('article', )
    date_hierarchy = 'date'
    ordering       = ('-date', )
    search_fields = ('pseudo', 'email', )

      # Colonnes personnalisées 
    def apercu_contenu(self, comment):
        """ 
        Retourne les 40 premiers caractères d'un commentaire. S'il
        y a plus de 40 caractères, il faut rajouter des points de suspension.
        """
        text = comment.contenu[0:40]
        if len(comment.contenu) > 40:
            return '%s…' % text
        else:
            return text

    apercu_contenu.short_description = 'Aperçu du contenu'



admin.site.register(Article, ArticleAdmin)
admin.site.register(Categorie)
admin.site.register(Comment,CommentAdmin)