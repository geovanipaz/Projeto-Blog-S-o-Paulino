from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='post_autor')
    blog_titulo = models.CharField(max_length=264, verbose_name='Digite um título')
    slug = models.SlugField(max_length=264, unique=True)
    blog_conteudo = models.TextField(verbose_name='Escreva algo')
    blog_imagem = models.ImageField(upload_to='blog_images',
                                    verbose_name='Imagem do Blog')
    data_publicacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.blog_titulo
    
class Comentario(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, 
                             related_name='blog_comentario')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, 
                                related_name='usuario_comentario')
    comentario = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)
    
class Gostei(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, 
                             related_name='gostei_blog')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, 
                                related_name='usuarios_gostaram')